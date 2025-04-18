# 🚧 RoadDesignOptimizer 🚧

[![Streamlit](https://img.shields.io/badge/Powered%20by-Streamlit-blue)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Built%20with-Python-red)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## Overview

RoadDesignOptimizer is a **Streamlit-based web application** designed to assist highway engineers in optimizing road geometric designs. It processes user-uploaded CAD files and design parameters to generate optimized horizontal alignment, vertical profiles, and superelevation calculations in compliance with the **Ethiopian Roads Authority (ERA)** geometric design standards.

This tool is ideal for engineers working on road projects in Ethiopia or regions following similar standards. It ensures that all designs meet ERA requirements for minimum radii, gradients, sight distances, and superelevation rates.

---

## Features

✅ **Horizontal Alignment Optimization**  
- Validates and optimizes proposed horizontal alignments based on ERA standards.
- Ensures compliance with minimum radii, tangent lengths, stopping sight distance (SSD), and K-values.

✅ **Vertical Profile Optimization**  
- Generates vertical curves (crest and sag) based on design speed, gradients, and K-values.
- Ensures smooth transitions and proper drainage gradients.

✅ **Superelevation Calculations**  
- Calculates superelevation rates and runoff lengths for horizontal curves.
- Handles transitions between normal crown sections and full superelevation.

✅ **Compliance with ERA Standards**  
- Uses tables and formulas from the **ERA Geometric Design Manual** for all calculations.

✅ **Downloadable Outputs**  
- Horizontal alignment coordinates (CSV/Excel).
- Vertical profile data (TXT/CSV).
- Superelevation rates (CSV).

---

## Installation

### Prerequisites

- Python 3.8 or higher
- Git

### Steps to Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/RoadDesignOptimizer.git
   cd RoadDesignOptimizer
   ``
   Usage
Input Requirements
CAD Files
Upload CAD files containing:
Proposed horizontal alignment.
Existing surface profile.
Design Parameters
Select the following:
Design speed (e.g., 30 km/h, 50 km/h, etc.).
Road design class (DC8 to DC1 for paved/unpaved roads as per ERA standards).
Terrain type (Flat, Rolling, Mountainous, Escarpment, Urban/Peri-Urban).
Optional Inputs
Right-of-way constraints.
Drainage requirements.
Output Downloads
After processing, you can download the following outputs:

Horizontal Alignment : CSV/Excel file with Northing and Easting coordinates.
Vertical Profile : TXT/CSV file with station, elevation, and curve data.
Superelevation : CSV file with superelevation rates and runoff lengths.
Folder Structure
 ```bash
road_design_optimizer/
│
├── app/                     # Main application folder
│   ├── __init__.py          # Makes this folder a Python package
│   ├── main.py              # Entry point for the Streamlit app
│   ├── horizontal_alignment.py  # Logic for horizontal alignment optimization
│   ├── vertical_profile.py       # Logic for vertical profile optimization
│   ├── superelevation.py         # Logic for superelevation calculations
│   └── utils.py                  # Utility functions (e.g., CAD parsing, ERA standards)
│
├── data/                    # Folder for input/output data
│   ├── input_cad_files/     # User-uploaded CAD files
│   └── output_files/        # Generated output files (CSV, TXT, etc.)
│
├── tests/                   # Unit tests for the application
│   └── test_utils.py        # Example test file
│
├── requirements.txt         # List of Python dependencies
├── README.md                # Project documentation
└── venv/                    # Python virtual environment
   ```
## Dependencies
The following libraries are used in this project:

Streamlit : For building the web interface.
Pandas/Numpy : For data manipulation and calculations.
Matplotlib/Plotly : For visualizations (optional for now).
ezdxf : For parsing CAD files.
Contributing
Contributions are welcome! Please follow these steps:

## Fork the repository.
Create a new branch (git checkout -b feature/YourFeatureName).
Commit your changes (git commit -m "Add some feature").
Push to the branch (git push origin feature/YourFeatureName).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Ethiopian Roads Authority (ERA) : For providing the Geometric Design Manual.
Streamlit Community : For their excellent framework and resources.
Open Source Libraries : Special thanks to contributors of Pandas, Numpy, Matplotlib, and ezdxf.
Contact
For any questions or feedback, feel free to reach out:

GitHub Issues : Open an issue in this repository.
Email : email2yonatan@gmail.com
## Future Enhancements
Add support for additional CAD formats (e.g., DWG).
Include visualization of alignments and profiles directly in the app.
Implement advanced optimization algorithms for more efficient earthwork balance.
Add multi-language support for broader accessibility.
Made with ❤️ by Yonatan Abrham
