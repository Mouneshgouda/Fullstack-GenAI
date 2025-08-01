
## Energy Predictor

```python

import streamlit as st
import pandas as pd
import joblib
import datetime

# Page configuration
st.set_page_config(page_title="Energy Predictor", page_icon="⚡")
st.title("⚡ Energy Consumption Predictor")

# Load the trained model
model = joblib.load("Random_forest_model (2).pkl")


# Define model's expected input columns
model_columns = [
    'num_occupants',
    'house_size_sqft',
    'monthly_income',
    'outside_temp_celsius',
    'year',
    'month',
    'day',
    'season',
    'heating_type_Electric',
    'heating_type_Gas',
    'heating_type_None',
    'cooling_type_AC',
    'cooling_type_Fan',
    'cooling_type_None',
    'manual_override_Y',
    'manual_override_N',
    'is_weekend',
    'temp_above_avg',
    'income_per_person',
    'square_feet_per_person',
    'high_income_flag',
    'low_temp_flag',
    'season_spring',
    'season_summer',
    'season_fall',
    'season_winter',
    'day_of_week_0',
    'day_of_week_6',
    'energy_star_home'
]

# Input form
with st.form("user_inputs"):
    st.header("📝 Enter Input Data")

    col1, col2 = st.columns(2)
    with col1:
        num_occupants = st.number_input("Occupants", min_value=1, value=3)
        house_size = st.number_input("House Size (sqft)", min_value=100, value=1500)
        income = st.number_input("Monthly Income", min_value=1000, value=40000)
        temp = st.number_input("Outside Temp (°C)", value=22.0)
    with col2:
        date = st.date_input("Date", value=datetime.date.today())
        heating = st.selectbox("Heating Type", ["Electric", "Gas", "None"])
        cooling = st.selectbox("Cooling Type", ["AC", "Fan", "None"])
        manual = st.radio("Manual Override", ["Yes", "No"])
        energy_star = st.checkbox("Energy Star Certified Home")

    submitted = st.form_submit_button("🔮 Predict")

# On form submit
if submitted:
    try:
        # Derived features
        day_of_week = date.weekday()
        season_label = {
            12: 'winter', 1: 'winter', 2: 'winter',
            3: 'spring', 4: 'spring', 5: 'spring',
            6: 'summer', 7: 'summer', 8: 'summer'
        }.get(date.month, 'fall')

        # Feature dictionary
        features = {
            'num_occupants': num_occupants,
            'house_size_sqft': house_size,
            'monthly_income': income,
            'outside_temp_celsius': temp,
            'year': date.year,
            'month': date.month,
            'day': date.day,
            'season': {'spring': 2, 'summer': 3, 'fall': 4, 'winter': 1}[season_label],
            'heating_type_Electric': int(heating == "Electric"),
            'heating_type_Gas': int(heating == "Gas"),
            'heating_type_None': int(heating == "None"),
            'cooling_type_AC': int(cooling == "AC"),
            'cooling_type_Fan': int(cooling == "Fan"),
            'cooling_type_None': int(cooling == "None"),
            'manual_override_Y': int(manual == "Yes"),
            'manual_override_N': int(manual == "No"),
            'is_weekend': int(day_of_week >= 5),
            'temp_above_avg': int(temp > 22),
            'income_per_person': income / num_occupants,
            'square_feet_per_person': house_size / num_occupants,
            'high_income_flag': int(income > 40000),
            'low_temp_flag': int(temp < 15),
            'season_spring': int(season_label == "spring"),
            'season_summer': int(season_label == "summer"),
            'season_fall': int(season_label == "fall"),
            'season_winter': int(season_label == "winter"),
            'day_of_week_0': int(day_of_week == 0),
            'day_of_week_6': int(day_of_week == 6),
            'energy_star_home': int(energy_star)
        }

        # Convert to DataFrame and match model columns
        df = pd.DataFrame([{col: features.get(col, 0) for col in model_columns}])

        # Predict
        prediction = model.predict(df)[0]
        st.success(f"🔋 Estimated Energy Usage: **{prediction:.2f} kWh**")

    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
```
