# Medical Data Visualizer

A **freeCodeCamp – Data Analysis with Python** certification project.

## Overview

Visualizes medical examination data using **Pandas**, **Seaborn**, and
**Matplotlib** to explore relationships between cardiovascular disease, body
measurements, blood markers, and lifestyle choices.

## Charts produced

### 1. Categorical Plot (`catplot.png`)
Shows value counts of `cholesterol`, `gluc`, `smoke`, `alco`, `active`, and
`overweight` split by `cardio` (0 = no disease, 1 = disease present).

### 2. Correlation Heatmap (`heatmap.png`)
Lower-triangle correlation matrix of all features after cleaning outliers.

## Dataset

Download **`medical_examination.csv`** from the freeCodeCamp boilerplate and
place it in the project root:

```
https://github.com/freeCodeCamp/boilerplate-medical-data-visualizer
```

The file uses **semicolons** as the delimiter and has these columns:

```
age, height, weight, gender, ap_hi, ap_lo,
cholesterol, gluc, smoke, alco, active, cardio
```

## Data transformations

| Step | Description |
|------|-------------|
| Overweight | BMI > 25 → 1, else 0  (BMI = weight / (height/100)²) |
| Cholesterol | 1 → 0 (normal), > 1 → 1 (elevated) |
| Glucose | 1 → 0 (normal), > 1 → 1 (elevated) |
| Heatmap cleaning | Remove rows where ap_lo > ap_hi, or height/weight outside 2.5–97.5 percentile |

## Requirements

```bash
pip install pandas matplotlib seaborn numpy
```

## Usage

```bash
python main.py
# outputs catplot.png and heatmap.png
```

