# Assignment 4: Reflection

## What Worked Well
The Streamlit interface successfully turned a static dataset into a guided narrative. The use of `@st.cache` significantly improved performance when loading the NASA Gold dataset. Integrating the weather data allowed for the creation of meaningful categorical groups (like `is_hot`), which made the Chi-Square analysis much more insightful than looking at continuous numbers alone.

## Challenges & Difficulties
A major challenge was the distribution of the NASA `event_count`. Since many days have zero events, the data is highly skewed. This made the T-test assumptions of normality difficult to satisfy perfectly. Additionally, converting local paths to relative paths for deployment required careful repository organization.

## Statistical Assumptions & Limitations
1. **Independence:** Weather data is inherently temporal. Today’s temperature is often related to yesterday’s, which can violate the independence assumption required for some tests.
2. **Causation:** While we found correlations between temperature and event counts, these are associations. High temperature might correlate with wildfires, but it doesn't account for other factors like human activity or lightning.
3. **Join Strategy:** Joining strictly on `date` assumes that the weather recorded for that day is the immediate driver of the event, ignoring potential "lag effects" (e.g., a drought a week ago causing a fire today).

## Future Improvements
If I were to expand this, I would implement **Non-Parametric tests** (like the Mann-Whitney U test) to better handle the skewed event data. I would also add a geographical component to the join, linking NASA events to specific local weather stations rather than global averages.