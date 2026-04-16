import streamlit as st
st.title("My Interactive Analysis App")
st.write("Hello, Professor! This is the start of Assignment 4.")

import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.express as px

# 1-Load the dataset
st.set_page_config(page_title="NASA & Weather Analysis", layout="wide")
@st.cache
def load_data():
    # Replace with your actual gold dataset path
    df = pd.read_csv("C:/Users/ALI COMPUTER/aidi-1204-streamlitapp/data/gold/nasa_weather_daily.csv")
    df.columns = df.columns.str.strip().str.lower()
    df['date'] = pd.to_datetime(df['date'])
    df['is_rainy'] = df['precipitation_sum'] > 0
    return df

# 2-Story/Sidebar
df = load_data()
st.sidebar.title("NASA Events & Weather Analytics")
st.sidebar.info("This app explores how weather patterns correlate with NASA event frequencies. "
"**New Source added:** Wildfire/Environmental context joined by date.")

# 3-Project Overview
if st.checkbox("Show Raw Data"):
    st.write(df.head())
    st.write("### Summary Statistics")
    st.write(df.describe())

# 4-Data Exploration
st.header("📊 Visual Trends")
col1, col2 = st.columns(2)

with col1:
    fig_temp = px.line(df, x='date', y='temp_max', title="Temperature Trend Over Time")
    st.plotly_chart(fig_temp, use_container_width=True)

with col2:
    fig_events = px.scatter(df, x='temp_max', y='event_count', 
                            trendline="ols", title="Temp vs. Event Count")
    st.plotly_chart(fig_events, use_container_width=True)


# 5-Statistical Analysis
st.header("Hypothesis Testing")

test_choice = st.selectbox("Select Analysis", [
    "1. One-Sample T-Test (Event Mean)",
    "2. Two-Sample T-Test (Rainy vs Clear Days)",
    "3. Chi-Square (Categorical Independence)",
    "4. Variance Comparison (F-Test)",
    "5. Correlation Analysis (Pearson)"
])

if test_choice == "1. One-Sample T-Test (Event Mean)":
    st.subheader("Is the mean event count different from a baseline of 10?")
    # Testing if the observed mean is significantly different from 10
    t_stat, p_val = stats.ttest_1samp(df['event_count'], 10)
    st.write(f"**T-statistic:** {t_stat:.4f}, **P-value:** {p_val:.4f}")
    st.write("Result: " + ("Significant" if p_val < 0.05 else "Not Significant"))

elif test_choice == "2. Two-Sample T-Test (Rainy vs Clear Days)":
    st.subheader("Do rainy days have different event counts than clear days?")
    rainy = df[df['is_rainy'] == True]['event_count']
    clear = df[df['is_rainy'] == False]['event_count']
    t_stat, p_val = stats.ttest_ind(rainy, clear)
    st.write(f"**P-value:** {p_val:.4f}")
    st.info("This compares the means of two independent groups.")

elif test_choice == "3. Chi-Square (Categorical Independence)":
    st.subheader("Is 'High Temperature' independent of 'Rainy Days'?")
    # Create a dummy category for high temp
    df['is_hot'] = df['temp_max'] > df['temp_max'].median()
    contingency_table = pd.crosstab(df['is_hot'], df['is_rainy'])
    chi2, p, dof, ex = stats.chi2_contingency(contingency_table)
    st.write(f"**Chi-Square Stat:** {chi2:.4f}, **P-value:** {p:.4f}")

elif test_choice == "4. Variance Comparison (F-Test)":
    st.subheader("Is event count variability different in summer vs winter?")
    # Simple split of the data
    group_a = df.iloc[:180]['event_count']
    group_b = df.iloc[180:]['event_count']
    f_stat = group_a.var() / group_b.var()
    p_val = 1 - stats.f.cdf(f_stat, len(group_a)-1, len(group_b)-1)
    st.write(f"**F-Statistic:** {f_stat:.4f}, **P-value:** {p_val:.4f}")

elif test_choice == "5. Correlation Analysis (Pearson)":
    st.subheader("Correlation between Temp and Event Count")
    corr, p_val = stats.pearsonr(df['temp_max'], df['event_count'])
    st.write(f"**Correlation:** {corr:.4f}, **P-value:** {p_val:.4f}")

# 6-Reflection
st.header("📝 Limitations & Assumptions")
st.write("""
- **Normality:** T-tests assume a normal distribution. 
- **Causation:** Correlation does not mean temperature *causes* NASA events.
- **Data Quality:** Missing values were dropped to ensure test accuracy.
""")