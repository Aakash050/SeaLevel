Sea Level 

## Problem Statement
Find accurate ways of predicting sea level in next 15 - 25 years.

## Dataset
- Name: `epa-sea-level.csv`
- Size/shape: 134 x 5
- Key features used: Year,CSIRO Adjusted Sea Level

## Methods
- Preprocessing: Dropped missing values, filtered to years greater than or equal to 2000
- Models tried: Linear Regression, SVM

## Metrics
- MSE
- Linear MSE: 0.0227
- SVM MSE: 0.0254

## Takeaways
- LR worked better, predicted sea level rise of 13.7 inches

## Repro
```
pip install -r requirements.txt
jupyter lab
# Open notebooks/project_notebook_clean.ipynb and run all
```

