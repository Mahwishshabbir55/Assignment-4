# Assignment 4: Analysis Plan
**Project:** NASA Events & Weather Analytics Correlation

## 1. New Data Source & Extension
- **Source Name:** Global Environmental Event Tracker (Wildfire Data Integration)
- **Join Key:** `date`
- **New Derived Variables:** - `is_rainy`: Boolean flag derived from `precipitation_sum > 0`.
    - `is_hot`: Categorical flag created via median split of `temp_max` (for Chi-Square).
    - `event_day`: Binary indicator of whether NASA recorded an event.
- **Story Goal:** This project investigates if specific weather conditions (temperature, precipitation) are statistically significant predictors or correlates of NASA-tracked environmental events and wildfires.

## 2. Planned Statistical Analyses

### A. T-Tests
1. **One-Sample T-Test:** Is the mean daily NASA `event_count` significantly different from a baseline of 0.5? 
2. **Two-Sample T-Test:** Does the `temp_max` differ significantly between days with NASA events (`event_day` = 1) and days without?

### B. Categorical Analysis (Chi-Square)
- **Test:** Chi-Square Test of Independence.
- **Variables:** `is_hot` vs `is_rainy`.
- **Question:** Is the occurrence of high-temperature days independent of rainy days within this event window?

### C. Variance Comparison (F-Test)
- **Question:** Is the variability (variance) of `event_count` different between the first half and second half of the dataset (proxy for seasonal change)?

### D. Correlation Analysis
- **Method:** Pearson Correlation.
- **Variables:** `temp_max` and `event_count`.
- **Question:** Is there a linear relationship between heat intensity and the number of global events recorded?

## 3. Supporting Visualizations
- **Time-Series:** Showing `temp_max` and `event_count` trends.
- **Boxplot:** Visualizing `temp_max` distributions grouped by `event_day` to motivate the T-Test.
- **Scatter Plot:** Showing the correlation between temperature and event frequency.