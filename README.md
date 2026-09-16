# 🛣️ RoadOptimizer
### Computational Highway Alignment & Superelevation Optimization Suite

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Standard](https://img.shields.io/badge/Standard-ERA%202013%20%2F%20AASHTO-008080?style=for-the-badge)](#standards-compliance)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

**RoadOptimizer** is an interactive, web-based computational engineering tool designed for highway and transportation engineers. It streamlines the geometric road design workflow by parsing raw CAD data, automating horizontal curve and vertical profile alignment optimizations, and computing standard-compliant superelevation runoffs.

---

## 🌟 Key Capabilities

* 📂 **Direct CAD / DXF Ingestion:** Parses road alignment entities, contour surfaces, and point datasets directly from AutoCAD/Civil 3D DXF files using `ezdxf`.
* 🔄 **Horizontal Alignment Optimization:** Computes curve radii, transition spirals, deflection angles, and coordinates ($PC$, $PI$, $PT$) according to target design speeds.
* 📈 **Vertical Profile Modeling:** Evaluates crest and sag vertical curve lengths, calculates $K$-values, and visualizes grade lines over natural ground terrain.
* ⚖️ **Superelevation & Standard Verification:** Automatically computes required superelevation rates ($e_{max} = 4\%, 6\%, 8\%$) and transition runoff lengths in strict compliance with the **Ethiopian Roads Administration (ERA 2013 Manual)** and **AASHTO Green Book**.
* 📊 **Interactive 3D & 2D Visualizations:** Dynamic interactive plotting powered by **Plotly** and **Streamlit** for real-time engineering feedback.

---

## 🏗️ Architecture & Module Structure

```
RoadOptimizer/
├── app.py                     # Streamlit application entry point & navigation
├── pages/
│   ├── Upload_Data.py         # Survey, DXF, and CSV coordinate ingestion
│   ├── Horizontal_Optimization.py # Horizontal curve geometry & radius checks
│   ├── Vertical_Optimization.py   # Vertical crest/sag curve fitting & grade checks
│   └── Both_Optimization.py       # Integrated 3D corridor alignment
├── src/
│   ├── design_standards.py    # ERA 2013 / AASHTO design speed & curvature lookups
│   ├── file_handler.py        # DXF / CSV parser and data validator
│   ├── optimization.py        # Numerical optimization algorithms (SciPy)
│   └── utils.py               # Geometric transformations & helper utilities
└── requirements.txt           # Environment dependencies
```

---

## 🚀 Quick Start

### 1. Prerequisites
Ensure you have Python 3.10+ installed.

### 2. Clone the Repository
```bash
git clone https://github.com/YonInsights/RoadOptimizer.git
cd RoadOptimizer
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the Web Application
```bash
streamlit run app.py
```
Open `http://localhost:8501` in your browser.

---

## 📐 Standards Compliance

RoadOptimizer checks geometric parameters against standard design criteria:
* **Ethiopian Roads Authority (ERA 2013):** Geometric Design Manual (Vol. I & II).
* **AASHTO A Policy on Geometric Design of Highways and Streets:** Stopping Sight Distance (SSD), Passing Sight Distance (PSD), and maximum relative gradients.

---

## 👨‍💻 Author

**Yonatan Abrham**  
*Highway Design Engineer & Infrastructure Technologist*  
* Founder & Developer of [Infradigital CAD](https://www.infradigitalcad.com/)
* LinkedIn: [linkedin.com/in/yonatan-abrham1](https://www.linkedin.com/in/yonatan-abrham1/)
* Email: [email2yonatan@gmail.com](mailto:email2yonatan@gmail.com)
