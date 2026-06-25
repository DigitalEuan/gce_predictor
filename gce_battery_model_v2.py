import math
from dataclasses import dataclass

@dataclass
class DualSolarDay:
    doy: int
    # Fast store inputs (Flares, CMEs)
    q_xray: float
    q_cme: float
    # Slow store inputs (CH HSS, Dst, Kp)
    q_kp: float
    q_bz: float
    q_ch_hss: float
    q_dst: float

class DualBatteryState:
    def __init__(self, site_key: str, c_site: float, r_site: float):
        self.site_key = site_key
        self.c_site = c_site
        self.r_site = r_site
        
        # CAL-03 Resolution: Dual compartments
        self.tau_fast = 0.5  # days (ionospheric)
        self.tau_slow = c_site * r_site  # days (geological)
        
        self.Q_f = 0.0
        self.Q_s = 0.0
        self.predicted_geometry = "Identity (Rest)"
        self.discharged = False
        
    def step(self, day: DualSolarDay):
        # 1. Add daily charge
        dQ_f = day.q_xray + day.q_cme
        dQ_s = day.q_kp + day.q_bz + day.q_ch_hss + day.q_dst
        
        # 2. RC Evolution
        self.Q_f = (self.Q_f + dQ_f) * math.exp(-1.0 / self.tau_fast)
        self.Q_s = (self.Q_s + dQ_s) * math.exp(-1.0 / self.tau_slow)
        
        # 3. UBP Integration (T-06 Resolution)
        total_Q = self.Q_f + self.Q_s
        n = int(total_Q * 1000) % (2**24)  # Map to 24-bit integer
        
        # Convert to Gray Code
        gray = n ^ (n >> 1)
        hw = bin(gray).count('1') # Hamming Weight
        
        # 4. Manifestation Logic
        if hw >= 4:
            self.discharge(hw)
            return True # GCE Event Occurred
            
        return False

    def discharge(self, hw: int):
        # CAL-01 Resolution: Partial discharge based on UBP structural tax
        # Using canonical NRCI values for Octad (0.7623) and Dodecad (0.6814)
        nrci = 0.7623 if hw == 8 else 0.6814 if hw == 12 else 0.6160
        dissipation_ratio = 1.0 - nrci
        
        # Fast store dissipates mostly, Slow store dissipates by UBP ratio
        self.Q_f = self.Q_f * 0.10 
        self.Q_s = self.Q_s * dissipation_ratio
        
        # T-06 Resolution: Geometry Mapping based on Trajectory
        if self.Q_f > self.Q_s:
            self.predicted_geometry = "Octad (Simple Circle/Ring)"
        else:
            self.predicted_geometry = "Dodecad (Complex Pictogram)"
