# Meta-Regression & Predictive Modeling of Cardiovascular Disease Risk

This repository presents a statistical modeling project conducted as part of Columbia University's Linear Algebra and Probability course. The study investigates the relationship between carotid intima-media thickness (cIMT) progression and cardiovascular disease (CVD) risk by applying Ordinary Least Squares (OLS) and Weighted Least Squares (WLS) regression models.

## Project Objective

To perform a meta-regression analysis using published studies and identify significant clinical and demographic cofactors that influence the association between cIMT progression and CVD risk.

## Key Features

- Reproduces prior meta-analysis using OLS and extends with WLS to handle heteroscedasticity.
- Investigates multiple cofactors such as age, sex, follow-up duration, and trial size.
- Provides code-based predictions and summary statistics for medical risk interpretation.

## Project Structure

This repository implements a meta-regression and predictive model to analyze cardiovascular disease risk based on aggregated clinical data.

```
.
├── README.md # Project overview and instructions
├── .gitignore # Ignore temporary/system files
├── requirements.txt # Python dependencies
├── code/
│ └── main.py # Core script: loads data, performs OLS/WLS regression, and prediction
├── data/
│ └── all_study_data_combined.csv # Cleaned dataset with effect sizes, demographics, and confidence intervals
├── docs/
│ └── Main_Project_Report.pdf # Full course project write-up (includes methodology, visuals, and interpretation)
```

## Models Used

- **OLS Regression**: Establishes baseline relationships
- **WLS Regression**: Weights each study by inverse variance to account for data reliability
- **Prediction Module**: Applies trained model on new study input for risk projection

## References

- Willeit et al. (2020) - [Circulation](https://doi.org/10.1161/CIRCULATIONAHA.120.046361)
- Harrer et al. (2021) - _Doing Meta-Analysis with R_
- Other academic and clinical sources as cited in `Main_Project_Report.pdf`

## Authors

Steven Hsiao, Cynthia Jin, Liang Yang — Columbia University

## License

```
Copyright © 2025 Steven Hsiao

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at:

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

---

## Relevance to Quantitative Finance

This project applied advanced linear algebra concepts and statistical inference, demonstrating strong quantitative analysis and technical programming skills. These capabilities are directly applicable to:

- Financial modeling  
- Signal extraction from noisy data  
- Algorithmic decision-making under uncertainty

Such skills are foundational in quantitative trading, particularly in areas like strategy backtesting, risk modeling, and real-time market analysis.
