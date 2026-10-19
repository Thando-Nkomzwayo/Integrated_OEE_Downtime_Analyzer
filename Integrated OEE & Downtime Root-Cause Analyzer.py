# Integrated OEE & Downtime Root-Cause Analyzer (v3.0)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17855209.svg)](https://doi.org/10.5281/zenodo.17855209)
![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-blue.svg)
![Excel: Enterprise v3.0](https://img.shields.io/badge/Excel-Enterprise_v3.0-green.svg)

An enterprise-grade, multi-metric decision-support model built on real industrial Internet-of-Things (IoT) production data from a continuous heavy clay (brick) manufacturing facility monitored via Evocon OEE software.

---

## 📌 Project Overview
Top-line Overall Equipment Effectiveness (OEE) metrics often fail to drive operational improvement unless mathematically linked to high-granularity loss categories and root-cause downtime events. This analyzer bridges the gap between raw shift monitoring and executive strategy by:
1. Re-deriving **Availability ($A$), Performance ($P$), and Quality ($Q$)** directly from underlying operating times and brick unit counts rather than relying on pre-calculated summary numbers.
2. Reconciling calculated OEE against source software logs row-by-row to guarantee 100.0% mathematical integrity.
3. Performing multi-dimensional **Pareto root-cause analysis** across 1,717 discrete downtime events.
4. Providing an interactive **Lean Six Sigma Scenario Simulator** to model the financial ROI (ZAR) of targeted downtime elimination strategies.

---

## 📊 Dataset Citation & Provenance
* **Dataset Title**: Overall Equipment Effectiveness and Downtime datasets in Heavy Clay production line
* **Source Repository**: Zenodo (CERN-hosted) | **Record ID**: `17855209`
* **DOI**: [10.5281/zenodo.17855209](https://doi.org/10.5281/zenodo.17855209)
* **Collection Window**: September 22, 2025 – December 18, 2025 (88 Calendar Days / 176 Production Shifts)
* **Tracking Infrastructure**: Evocon Automated OEE Tracking Software
* **Scope**: 176 Shift Records | 1,717 Discrete Downtime Events | Heavy Clay Brick Manufacturing Line

---

## 🏗️ 10-Tab Model Architecture
1. **`README & Dataset Citation`**: Metadata, formal academic citation, cleaning protocol log, and cell protection map.
2. **`Raw Data (Reference)`**: Untouched, immutable audit reference copy of original ingested Evocon exports.
3. **`Shift Data Entry`**: Validated operational tracker containing 176 shift records with full time components in seconds.
4. **`Downtime Data Entry`**: Event-level operational log containing 1,717 discrete stop records mapped to standardized English taxonomy.
5. **`Calculation Engine`**: Backend reconciliation engine re-deriving $A \times P \times Q$ and verifying 100.0% row-by-row match against source OEE.
6. **`Downtime Root-Cause Analysis`**: Multi-dimensional Pareto analytics by Stop Reason, Location, and Duration.
7. **`Executive Dashboard`**: C-Suite visual dashboard featuring 5 KPI tiles, RAG status cards, SPC shift trend chart, and Lean Six Sigma comparison matrix.
8. **`Scenario Simulator`**: Interactive sensitivity environment modeling downtime reduction levers and financial ROI in ZAR.
9. **`Exception Log & Action Plan`**: Automated alert engine anchored in dataset percentiles ($p_{25}$, $p_{90}$, $p_{10}$) with CAPA action tracking.
10. **`Methodology & Improvement Log`**: TPM mathematical documentation, Greek-to-English translation dictionary, and continuous improvement audit log.

---

## 🧮 Mathematical Formulation (TPM Standard)
$$\text{Availability } (A) = \frac{\text{Planned Operating Time} - \text{Unplanned Downtime}}{\text{Planned Operating Time}}$$

$$\text{Performance } (P) = \frac{\text{Total Quantity} \times \text{Ideal Cycle Time (2.0s)}}{\text{Operating Time}}$$

$$\text{Quality } (Q) = \frac{\text{Good Quantity}}{\text{Total Quantity}}$$

$$\text{Overall Equipment Effectiveness } (\text{OEE}) = A \times P \times Q$$

---

## 🔍 Key Findings & Empirical LSS Breakpoint
* **Statistical Process Control (SPC) Breakpoint**: Identified cleanly at **Shift 89** (November 10, 2025).
* **Phase 1 (Pre-LSS Baseline | Shifts 1–88)**: Mean OEE = **68.4%** (Availability 74.2%, Performance 93.1%, Quality 98.9%).
* **Phase 2 (Post-LSS Actual | Shifts 89–176)**: Mean OEE = **79.1%** (Availability 84.8%, Performance 95.2%, Quality 98.0%).
* **Top Downtime Cost Drivers**: *Extruder Mechanical Breakdown* (247 events / 14.4%) and *Raw Material Clay Shortage* (206 events / 12.0%).

---

## ⚠️ Operational Scope & Data Limitations
1. **Single Line Scope**: Data represents a single continuous heavy clay extrusion line; thermal inertia and moisture sensitivities reflect heavy ceramics rather than high-speed assembly.
2. **Financial Parameterization**: Hourly plant operating cost rate (default R 4,500.00/hr) is a parameterized user input applied to real downtime hours.
3. **Statistical Breakpoint**: The Pre/Post Lean Six Sigma split is statistically inferred via 14-shift rolling average SPC trend analysis at Shift 89.

---

## 📜 License
This dataset and analytical model are distributed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.