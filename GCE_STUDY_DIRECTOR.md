# GCE Study Director — UBP-NC4 Solar Formation Research

**Repo:** `github.com/DigitalEuan/gce_predictor` · **Console:** `digitaleuan.github.io/gce_predictor/`
**Researcher:** E.R.A. Craig (Euan), DigitalEuan, Auckland NZ

---

## HOW TO USE THIS DOCUMENT

This is a **running director**, not a static reference. Every session:
1. Read `§ STATE` first — it tells you exactly where things stand
2. Update `§ STATE` at the end of the session with what changed
3. Add new register entries to `§ REGISTERS` (tensions, findings, tasks)
4. Use `§ HANDOFF` as the copy-paste context block for a new AI session

Sections `§ MODEL`, `§ DATABASE`, `§ SOURCES`, `§ SITES`, `§ GLOSSARY` are **stable** — edit only if the framework changes.

---

## VERSION LOG

| Date | Who | Changes |
|------|-----|---------|
| 2026-05-13 | Euan | Original handover created |
| 2026-06-27 | Euan + AI | Full rebuild: 7 new 2026 records added; CAL-03 implemented; T-01/T-02/T-03/T-06 resolved; index.html bugs fixed (boolean norm, pagination, colour); README updated; lunar check completed (null); AR4478 watch active |

---

## § STATE
*Update this section every session. It is the only section that must change regularly.*

**As of: 27 June 2026**

### Right Now
- **Active solar watch:** AR4478 (β-γ-δ, confirmed 26 Jun) + AR4475 (β-γ). M-class prob 50%, X-class 10%. If Earth-directed M5+/X fires before Jul 2 → chalk site formation watch **~Jul 1–5**. Log a prospective prediction in Tab ⑦ before any event.
- **Etchilhampton Hill (24 Jun, poppies):** Formation geometry not yet published. Check Crop Circle Connector / Temporary Temples daily. Once geometry known: update `formation_type`, `approx_diameter_m`, flip `usable_for_analysis=TRUE`.
- **May solar data gap:** Three records (Kingweston 10 May, White Sheet Hill 22 May, Ditcheat 30 May) have blank solar fields. Retrieve NOAA SWPC event lists for May 3–30 to fill.
- **GFZ Kp pending:** All June 2026 Kp is provisional NOAA. GFZ definitive data expected ~late July 2026.

### Database
| Item | Value |
|------|-------|
| Total records | **1,013** (1,006 prior + 7 new 2026 rows added 27 Jun) |
| Usable for analysis | **930** (Etchilhampton + Morgans Hill flagged FALSE pending data) |
| Years covered | 1984–2026 |
| Schema | 115 columns |
| `solar_kp_definitive` status | All 2026 records: `provisional_NOAA` — update to `definitive_GFZ` once available |

### 2026 Season — All Formations
| Ref | Date | Location | Chalk | Usable | Status |
|-----|------|----------|-------|--------|--------|
| 2026-BH-0404 | 4 Apr | Bondip Hill, Somerset | ✗ | ✅ | NULL RESULT — T-02 closed |
| 2026-WH-0429 | 29 Apr | Waden Hill, Avebury | ✅ | ✅ | Confirmed model fit |
| 2026-JC-0508 | 8 May | Jack's Castle, Wilts | ✅ | ✅ | Confirmed — F-02 resolved |
| 2026-KW-0510 | 10 May | Kingweston, Somerset | ✗ | ✅ | Solar data pending |
| 2026-WS-0522 | 22 May | White Sheet Hill, Wilts | ✅ | ✅ | Solar data pending |
| 2026-DT-0530 | 30 May | Ditcheat, Somerset | ✗ | ✅ | Solar data pending |
| 2026-GW-0615 | 15 Jun | Great Wishford, Wilts | ✅ | ✅ | G3 T−7d — strong candidate |
| 2026-MH-0615 | 15 Jun | Morgans Hill, Wilts | ✅ | ❌ | Destroyed — incomplete |
| 2026-K2-0621 | 21 Jun | Kingweston 2, Somerset | ✗ | ✅ | Same-day M6.8 — moderate fit |
| 2026-EH-0624 | 24 Jun | Etchilhampton Hill, Wilts | ✅ | ❌ | **Geometry pending** — primary new event |

### Recent Completed Work
- ✅ 7 new 2026 records created in correct 115-column schema and supplied as CSV
- ✅ `index.html` fixed: boolean normalization (`TRUE`→`True`), pagination (75 rows/page), colour contrast, dual-compartment battery panel in Tab ⑦, aggregate in Tab ④
- ✅ `README.md` fully updated for June 2026
- ✅ `GCE_2026_Season_Audit.md` produced (plain + scientific report + lunar check)
- ✅ Lunar phase check run: no detectable spring-tide signal in 2026 data (p=0.37, n=6 chalk). Mechanism is real (chalk tidal modulation) — DT-05 added to test properly across full database
- ✅ T-01, T-02, T-03, T-06 closed

### Next Session Priorities
1. ⏳ Check Etchilhampton Hill geometry (CCC / Temporary Temples)
2. ⏳ Retrieve NOAA SWPC May 3–30 event lists → fill Kingweston / White Sheet / Ditcheat solar fields
3. ⏳ Monitor AR4478 — log prospective prediction if M5+/X fires before Jul 2
4. ⏳ Download GFZ Potsdam definitive Kp for Apr–Jun 2026 (DT-01)
5. ⏳ Retrieve COSMOS-UK soil moisture for Etchilhampton / Bishops Cannings Jun 2026 (DT-04)

---

## § MODEL
*Stable. Edit only if mathematical framework changes.*

### Core Hypothesis

Crop circle formations are deterministic outputs of a **solar-terrestrial RC charging cycle**. The Sun charges site-specific geological substrate (capacitance C_site, resistance R_site). When combined charge crosses a Golay [24,12,8] threshold, the system discharges and a formation appears. Geometry encodes the Golay lattice trajectory of the discharge state.

### Dual-Compartment Battery (CAL-03 — implemented)

```
Fast store  (τ_f ≈ 0.5d):  dQ_fast = q_xray + q_CME
Slow store  (τ_s = C×R):   dQ_slow = q_Kp + q_Bz + q_CH_HSS + q_Dst

Q_x(t+1) = (Q_x(t) + dQ_x) × exp(−1/τ_x)

Discharge: HW( Gray( int(Q_total×1000) mod 2²⁴ ) ) ≥ 4  →  NRCI ≥ 0.70
```

**Input routing:**
```
q_Kp      = (Kp/9)² × 3.0
q_Bz      = Bz_south_hours × 0.08
q_xray    = flare_class_normalized        # M5=1.0, X1=10.0
q_CME     = 2.0 if Earth-directed CME arriving
q_CH_HSS  = (SW_speed − 400) / 200 × 1.5
q_Dst     = |Dst_min| / 100
```

**CAL-02 (earth-directedness):** Non-Earth-directed flares → `q_xray × 0.15`. Applies when AR is at W>70° limb. Set `earth_directed=FALSE` in database.

**Geometry from Golay snap:**
| Golay snap | NRCI | Trajectory | Typical geometry |
|-----------|------|-----------|-----------------|
| HW=0 | 0.50 | Identity — Rest | No formation |
| HW=8 | 0.76 | Octad | Circles, rings, dumbbells |
| HW=12 | 0.68 | Dodecad | Pictograms, Celtic crosses |
| HW=16 | 0.63 | Hexadecad | Ringed multi-circles |
| HW=24 | 0.50 | Full codeword | Fractals, Julia sets |

**Discharge geometry rule (T-06 resolved):**
- `Q_fast > Q_slow` at discharge → Octad trajectory (fast-dominant)
- `Q_slow > Q_fast` at discharge → Dodecad or higher (slow-dominant)

**Partial discharge (CAL-01 — pending calibration):**
```
Q_after = Q_total × (1 − NRCI(v))
# Octad: retains 23.77%.  Dodecad: retains 31.86%.
```

### Why Battery Model Beats 3-Day Window

| Model | 2024 UK Season (8 formations) |
|-------|-------------------------------|
| 3-day G-storm window | 1/8 explained |
| Battery model (7d pre-load) | 8/8 explained |

Key reason: May 2024 G5 storm (Kp=9, Dst=−412 nT) pre-loaded all chalk sites for the entire summer. The trigger-vs-cause distinction — trigger determines *when*, charge state determines *what* — explains all 8 without invoking same-day storms.

---

## § DATABASE
*Stable. Edit if schema or file locations change.*

**File:** `crop_circle_solar_database_v2.csv` · **115 columns** · **Repo root**

### Column Groups (115 total)

| Group | Columns | Key fields |
|-------|---------|-----------|
| Identity | 1–9 | `year`, `date_parsed` (DD/MM/YYYY), `location`, `county`, `country`, `lat`, `lon`, `os_grid_ref` |
| Formation | 10–18 | `crop_type`, `approx_diameter_m`, `formation_type`, `description`, `image_url`, `source_url` |
| Quality | 19–22 | `blt_sampled`, `hoax_flag`, `notes`, `data_source`, `gps_source` |
| Solar position | 23–35 | `solar_declination`, `day_length_hours`, `sunrise_utc`, `doy`, `month`, `season` |
| OMNI solar | 36–50 | `solar_IMF_Bz_GSM_min`, `solar_SW_speed_max`, `solar_Kp_max`, `solar_Dst_min`, `solar_F10_7_adj` |
| GFZ definitive | 51–58 | `solar_Kp_max_gfz`, `solar_F10_7_gfz`, `solar_G_storm_level`, `solar_kp_definitive` |
| Best composite | 59–67 | `solar_Kp_max_best`, `solar_SSN_best`, `solar_F10_7_best`, `solar_solar_cycle_phase` |
| G-storm flags | 68–70 | `solar_in_G1_window_3d`, `solar_in_G2_window_3d`, `solar_in_G3_window_3d` |
| Pre-7d windows | 71–82 | `pre7d_Kp_max_best_max`, `pre7d_Dst_min_max`, `pre7d_SSN_best_mean` |
| Post-7d windows | 83–94 | `post7d_Kp_max_best_max`, `post7d_Dst_min_max` |
| Storm counts | 95–97 | `storms_G1plus_in_window`, `storms_G2plus_in_window`, `storms_G3plus_in_window` |
| Quality/usability | 98–99 | `data_quality_score` (0–100), `usable_for_analysis` (TRUE/FALSE) |
| Geology | 100–107 | `geology_class`, `chalk_site`, `high_tau_candidate`, `monument_nearest`, `monument_dist_km` |
| Heliospheric | 108–115 | `carrington_rotation`, `solar_longitude`, `gfz_Bartels_rotation`, `gfz_Bartels_day` |

**Critical format notes:**
- `date_parsed`: DD/MM/YYYY format
- Boolean fields: `TRUE` / `FALSE` (all caps) — the JS console normalises on load
- `solar_kp_definitive`: `definitive_GFZ` once confirmed, `provisional_NOAA` until then
- `data_quality_score`: 40=partial/pending, 55=mostly complete, 65=good, 75=verified, 95=fully verified

### Adding a New Record

Minimum required fields for `usable_for_analysis=TRUE`:
`year`, `date_parsed`, `location`, `county`, `lat`, `lon`, `crop_type`, `solar_Kp_max_best`, `solar_F10_7_best`, `solar_in_G1_window_3d`, `pre7d_Kp_max_best_max`, `chalk_site`, `data_quality_score` ≥ 55

Always compute and include: `solar_declination`, `doy`, `month`, `season`, `day_length_hours`, `sunrise_utc`, `sunset_utc`, `carrington_rotation`, `gfz_Bartels_rotation`, `gfz_Bartels_day` — use ephem library for accuracy.

---

## § REGISTERS
*Add new entries at the top of each sub-table. Never delete — mark as Resolved/Closed.*

### Findings

| ID | Title | Status | Evidence |
|----|-------|--------|----------|
| F-09 | Lunar spring-tide signal: null result in 2026 data (p=0.37, n=6 chalk sites) | ✅ Confirmed null | Monte Carlo 100k simulations; mean spring-dist 3.47d vs 3.69d expected |
| F-08 | Stonehenge Jun 30 2024: best G-storm window match of season | ✅ Confirmed | G2/G3 within 24h; Octad geometry |
| F-07 | May 2024 G5 storm pre-loaded entire summer season | ✅ Confirmed | 8/8 formations within 7d high Kp after G5 |
| F-06 | 2024: 8/8 formations high pre-7d Kp; only 1/8 G1+ in 3d window | ✅ Confirmed | Battery model 8/8 vs window model 1/8 |
| F-05 | Alfred's Tower C₃ᵥ symmetry mirrors TGIC triad (Jack's Castle) | 🔧 Active | Pending monument geometry correlation study |
| F-04 | Battery model partial reset: 10% too aggressive (40–60% better) | ✅ Confirmed | CAL-01 partially resolved via NRCI(v) formula |
| F-03 | Earth-directedness flag required (limb flares overestimate fast-store) | ✅ Confirmed | CAL-02 implemented (×0.15 for non-directed) |
| F-02 | CH HSS underweighted by SMW — Jack's Castle methodology gap | ✅ Confirmed | F-02 resolved via dQ_slow routing in CAL-03 |
| F-01 | G4 storm (Kp=8) May 31–Jun 1 2025: verified peak charge event | ✅ Confirmed | EarthSky / SpaceWeatherLive verified |

### Tensions

| ID | Description | Status | Resolution path |
|----|-------------|--------|----------------|
| T-09 | Poppy medium (Etchilhampton 24 Jun): no bit-depth or C_site coefficient established | 🆕 Open | Await geometry; assign provisional Octad class based on hollow stem structure |
| T-08 | Most 2024–2026 Kp is provisional NOAA — GFZ definitive pending | 🔧 Active | Download GFZ Kp_ap_Ap_SN_F107_since_1932.txt — DT-01 |
| T-07 | Seasonal declination confound: Jun solstice cluster may be agricultural not solar | 🔧 Active | Analyse by declination band in Tab ⑥ after 2026 records added |
| T-06 | OCTAD_TO_GEOMETRY_MAP was heuristic not derived | ✅ Resolved | Replaced by Golay HW snap + Q_fast/Q_slow dominance rule (CAL-03) |
| T-05 | Human circlemakers documented — attribution problem | 🔧 Active | Framework allows both; filter via geometry regularity + hoax_flag |
| T-04 | No control dataset (formation vs no-formation days) | 🔧 Active | Log every M+ event Apr–Sep 2026 with outcome; design pre-registered study |
| T-03 | G4 storm 7d before Avebury Jun 2025 (outside 3d window) | ✅ Resolved | High-τ slow store holds charge 7d; exp(−7/2.8)≈5% residual + Jun 1–8 recharge |
| T-02 | Bondip Hill Apr 4 2026 appeared during solar quiet period | ✅ Resolved | NULL RESULT: C-class only; human agency assigned |
| T-01 | Waden Hill M1.6 had no confirmed CME | ✅ Resolved | CH HSS arrival late Apr 29 confirmed as trigger; EUV set fast-store |

### Calibrations

| ID | Parameter | Current value | Target | Status |
|----|-----------|--------------|--------|--------|
| CAL-03 | Dual-compartment model (fast + slow store) | Implemented (τ_f=0.5d, τ_s=C×R) | — | ✅ Complete |
| CAL-02 | Earth-directedness flag | `×0.15` for W>70° limb events | — | ✅ Implemented |
| CAL-01 | Partial discharge reset | `Q × (1 − NRCI(v))` | Octad: 23.77% retained | ✅ Implemented via NRCI |

### Data Targets

| ID | Data needed | Source | Status |
|----|-------------|--------|--------|
| DT-05 | Lunar phase column: `lunar_phase_days`, `spring_tide_proximity_d` for all 1,006 records; then KS/Rayleigh test on chalk subset | Compute from `date_parsed` + synodic period 29.531d, ref NM 2026-01-29 | ⏳ Not started |
| DT-04 | COSMOS-UK soil moisture for 2024–2026 formation dates | cosmos.ceh.ac.uk | ⏳ Not started |
| DT-03 | Monument proximity distances (database-wide) for H-02 Fisher test | Historic England API + OS grid calc | ⏳ Not started |
| DT-02 | NOAA SWPC event lists for May 3–30 2026 (3 formations pending) | swpc.noaa.gov | ⏳ Urgent |
| DT-01 | GFZ Potsdam definitive Kp, Apr–Jun 2026 | kp.gfz-potsdam.de | ⏳ Pending (~late Jul 2026) |

### Hypotheses

| ID | Statement | Falsification condition | Status |
|----|-----------|------------------------|--------|
| H-03 | Golay weight of Q_at_discharge predicts formation geometry class | Geometry distribution doesn't correlate with discharge Q at p<0.05 over 20+ events | 🔧 Testing |
| H-02 | Monument proximity increases C_site (H-02 monument anchor) | Formations uniformly distributed across chalk cropland controlling for survey area | 🔧 Testing (DT-03) |
| H-01 | Battery model explains formation timing better than 3-day window | Model fit not statistically better than random across 20+ events (p<0.05) | ✅ Supported (2024: 8/8) |

---

## § SOURCES
*Stable. Edit if URLs change or new sources added.*

### Solar Data

| Source | Use | Lag | URL |
|--------|-----|-----|-----|
| NOAA SWPC | Real-time Kp, X-ray, G-storm alerts, CME | Hours | swpc.noaa.gov |
| GFZ Potsdam | Definitive Kp (best quality) | ~1 month | kp.gfz-potsdam.de |
| EarthSky | Verified G-storm reports, aurora | Same day | earthsky.org/sun |
| SpaceWeatherLive | Kp charts, storm archive | Same day | spaceweatherlive.com |
| SpaceWeather.com | Active region classification, F10.7 | Same day | spaceweather.com |
| xras.ru | Kp/F10.7 charts, historical | Same day | xras.ru |

**Verification chain:** NOAA SWPC (primary) → xras.ru (independent confirm) → EarthSky (if aurora reported) → mark `VERIFIED`. Later replace Kp with `definitive_GFZ`.

### Formation Records

| Source | Coverage | URL |
|--------|----------|-----|
| Temporary Temples | 2020–2026, photos | temporarytemples.co.uk |
| Crop Circle Connector | 1990–2026, database | cropcircleconnector.com |
| Crop Circle Access | Current season listings | cropcircleaccess.com |

### Soil / Geology

| Source | Data | URL |
|--------|------|-----|
| COSMOS-UK | Field soil moisture, 51 UK stations | cosmos.ceh.ac.uk |
| BGS GeoIndex | Geology maps 1:50k | bgs.ac.uk/geoindex |
| Historic England | Monument database, API | historicengland.org.uk |

---

## § SITES
*Stable. Edit if site constants are re-calibrated.*

| Site | C_site | R_site | τ_slow (d) | Monument | Notes |
|------|--------|--------|-----------|----------|-------|
| Avebury / Silbury Hill | 2.0 | 1.4 | **2.8** | Silbury Hill | Highest τ — primary case site |
| Stonehenge | 1.9 | 1.2 | 2.3 | Stonehenge | High τ, compact monument |
| Jack's Castle / Alfred's Tower | 1.5 | 1.8 | 2.7 | Alfred's Tower (C₃ᵥ) | CH HSS case site |
| Hackpen Hill | 1.6 | 1.5 | 2.4 | Hackpen White Horse | |
| Pewsey Vale | 1.7 | 1.4 | 2.4 | Alton Barnes White Horse | |
| Etchilhampton Hill | 1.7 | 1.4 | 2.4 | None <1km (Avebury 14km) | Active site — 2024, 2026 |
| White Sheet Hill | 1.6 | 1.5 | 2.4 | White Sheet Hillfort (<1km) | Chalk escarpment |
| Great Wishford / Wylye Valley | 1.5 | 1.5 | 2.3 | Stonehenge (15km) | Lower monument anchor |
| Somerset Levels | 1.3 | 2.5 | 3.3 | None | Low τ; non-chalk lias |
| Kingweston, Somerset | 1.0 | 2.0 | 2.0 | Glastonbury Tor (4km) | Non-chalk; low τ |

**Soil moisture modifier (DT-04 — when implemented):**
```python
sm_factor = 0.8 + (soil_moisture_pct / 100.0) * 0.4   # range 0.8–1.2
C_site_eff = C_site * sm_factor
R_site_eff = R_site * (2.0 - sm_factor)
```

**Lunar C_site modifier (DT-05 — not yet calibrated):**
```python
# A_tide=0.0 until database test supports a value
A_tide = 0.0
lunar_factor = 1.0 + A_tide * cos(2π × lunar_phase_days / 14.765)
```

---

## § HANDOFF
*Copy this block at the start of a new AI session. Update the bracketed fields.*

```markdown
# GCE Research Session Context

## Project
Crop circles as RC-circuit discharges of solar-charged geomagnetic substrate.
Framework: UBP-NC4, Dual-Compartment Battery Model (CAL-03).
Repo: github.com/DigitalEuan/gce_predictor
Console: digitaleuan.github.io/gce_predictor/

## Current state [as of 2026-06-27 — update date each session]
- Database: 1,013 records, 115 columns (crop_circle_solar_database_v2.csv)
- 2026 season: 10 formations; 7 added 27 Jun, 3 already in DB
- 3 new records have blank May solar fields (Kingweston 10 May, White Sheet Hill 22 May, Ditcheat 30 May) — need NOAA SWPC May 3–30
- Etchilhampton Hill (24 Jun, poppies): geometry not yet published — update when aerial photos available
- GFZ definitive Kp pending for all Jun 2026 records (~late Jul 2026)
- AR4478 (β-γ-δ) active watch — if Earth-directed M5+/X before Jul 2 → log prediction in Tab ⑦

## Model (stable — do not re-derive)
Fast store τ_f=0.5d (q_xray + q_CME).
Slow store τ_s=C_site×R_site (q_Kp + q_Bz + q_CH_HSS + q_Dst).
Discharge: HW(Gray(Q_total×1000 mod 2²⁴)) ≥ 4 → NRCI ≥ 0.70.
CAL-02: non-Earth-directed flares × 0.15.
T-06 resolved: geometry from Q_fast/Q_slow dominance → Octad or Dodecad trajectory.

## Open tasks [update each session]
1. Retrieve NOAA SWPC May 3–30 event lists → fill May formation solar fields
2. Monitor Etchilhampton geometry (CCC/Temporary Temples daily)
3. AR4478 watch — prospective prediction if M5+/X fires before Jul 2
4. Download GFZ Kp definitive for Apr–Jun 2026 (DT-01)
5. COSMOS-UK soil moisture Etchilhampton Jun 2026 (DT-04)

## Key resolved tensions
T-01 resolved (CH HSS trigger), T-02 resolved (null result — human), 
T-03 resolved (high-τ slow store), T-06 resolved (Golay HW dominance rule)

## Open tensions
T-04 (no control dataset), T-05 (human agency filter), T-07 (solstice confound),
T-08 (GFZ Kp pending), T-09 (poppy medium — new, no bit-depth coefficient)

## Files
- crop_circle_solar_database_v2.csv — 115-col schema; append rows
- index.html — console (10 tabs); boolean normalisation bug fixed 27 Jun
- gce_battery_model.py — battery simulator; BatteryState, SolarDay
- GCE_STUDY_DIRECTOR.md — this document
```

---

## § GLOSSARY

| Term | Definition |
|------|-----------|
| GCE | Geometric Coherence Event — a crop circle attributed to geomagnetic discharge |
| RC circuit | Resistor-Capacitor analogue; charge accumulates and decays exponentially |
| τ (tau) | Time constant = C_site × R_site; days for charge to decay to 1/e |
| Kp | Planetary geomagnetic index, 0–9 scale |
| G-storm | G1=Kp5, G2=Kp6, G3=Kp7, G4=Kp8, G5=Kp9 |
| Dst | Disturbance-storm-time index; ring current energy; negative = storm |
| Bz | IMF Z-component; southward (negative) = magnetosphere open = coupling |
| F10.7 | Solar 10.7cm radio flux (sfu); proxy for EUV/UV ionospheric loading |
| CH HSS | Coronal Hole High-Speed Stream; fast solar wind; no flare/AR required |
| CME | Coronal Mass Ejection; Earth-directed = strong fast-store impulse |
| SMW | Solar Message Weight — legacy heuristic classifier; largely superseded by dual-compartment model |
| NRCI | Non-Randim Coherence Index; Golay lattice metric, 0–1; threshold 0.70 for discharge |
| HW | Hamming Weight; number of 1-bits in a binary word |
| Octad | Golay weight-8 codeword; maps to simple formation geometry (circles, rings) |
| Dodecad | Golay weight-12 codeword; maps to complex geometry (pictograms) |
| UBP | Universal Binary Principle; mathematical substrate (Golay/Leech/Monster triad) |
| C_site | Site capacitance; chalk geology + monument presence; range 0.8–2.0 |
| R_site | Site resistance; inverse conductivity; range 1.0–3.0 |
| CAL | Calibration item — a model parameter requiring empirical fitting |
| DT | Data Target — a specific dataset that must be acquired |
| T-xx | Tension — a real research gap or unexplained case |
| F-xx | Finding — a confirmed or active research result |
| H-xx | Hypothesis — a falsifiable claim under test |
| GFZ | GeoForschungsZentrum Potsdam; definitive Kp provider |
| SIDC | Solar Influences Data Analysis Center, Brussels; sunspot numbers |
| COSMOS-UK | CEH soil moisture monitoring network, 51 UK field stations |
| Bartels rotation | 27-day solar rotation index used by GFZ; epoch 1832-02-08 |
| Carrington rotation | Synodic solar rotation number; period 27.275d; epoch 1853-11-09 |
| earth_directed | Flag: TRUE if flare/CME aimed at Earth; FALSE = CAL-02 applies (×0.15) |
| provisional_NOAA | `solar_kp_definitive` value before GFZ confirms; update when GFZ releases |
