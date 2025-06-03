import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Load dataset
df = pd.read_csv("all_study_data_combined.csv")
print("Loaded data:")
print(df.head())

# --- OLS Regression ---
formula = '''
Q("effect size (RR)") ~ Q("No. of Patients per trial arm") + Q("Mean Age") + 
Q("% Female") + Q("CVD Risk Median Follow-Up Years") + 
Q("cIMT Progression Maximum Follow-Up Years") + Q("% with cIMT Data") + 
Q("cIMT progression per year")
'''
model_ols = ols(formula, data=df).fit()
print("\nOLS Regression Results:")
print(model_ols.summary())

# --- WLS Regression ---
data_copy = df.copy()
z = 1.96
data_copy["weight"] = ((2 * z) / (data_copy["upper CI"] - data_copy["lower CI"]))**2

X = data_copy[[
    "No. of Patients per trial arm", "Mean Age", "% Female",
    "CVD Risk Median Follow-Up Years", "cIMT Progression Maximum Follow-Up Years",
    "% with cIMT Data", "cIMT progression per year"
]]
X = sm.add_constant(X)
y = data_copy["effect size (RR)"]

wls_model = sm.WLS(y, X, weights=data_copy["weight"]).fit()
print("\nWLS Regression Results:")
print(wls_model.summary())

# --- Prediction on new data ---
new_data = pd.DataFrame({
    "No. of Patients per trial arm": [200, 300],
    "Mean Age": [55, 65],
    "% Female": [50, 60],
    "CVD Risk Median Follow-Up Years": [2.5, 3.5],
    "cIMT Progression Maximum Follow-Up Years": [4.0, 5.0],
    "% with cIMT Data": [80, 90],
    "cIMT progression per year": [10, 20]
})
new_data_with_const = sm.add_constant(new_data)
predictions = wls_model.predict(new_data_with_const)
new_data["Predicted Effect Size (RR)"] = predictions

print("\nPrediction on new data:")
print(new_data)