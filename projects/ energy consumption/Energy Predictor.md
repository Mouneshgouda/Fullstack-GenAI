
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

## Energy Predictor with Background 

```python


import streamlit as st
import pandas as pd
import joblib
import datetime
import plotly.graph_objects as go
import plotly.express as px

# Background & Styling
st.markdown("""
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1501785888041-af3ef285b470");
    background-size: cover;
    background-attachment: fixed;
    background-repeat: no-repeat;
}
.stApp::before {
    content: "";
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: rgba(0, 0, 0, 0.5);
    z-index: -1;
}
[data-testid="stForm"] {
    background-color: rgba(255, 255, 255, 0.08);
    padding: 2rem;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.2);
}
input, select, textarea {
    background-color: #f0f0f0 !important;
    color: #000 !important;
    border-radius: 8px !important;
    padding: 6px !important;
    border: 1px solid #ccc !important;
}
label, .stRadio > label, .stCheckbox, .css-1cpxqw2, .st-bf, .st-c9 {
    color: #ffffff !important;
    font-size: 16px !important;
}
h1, h2, h3 {
    color: white !important;
    font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Energy Predictor", page_icon="⚡")
st.title("⚡ Energy Consumption Predictor")

# Load model
model = joblib.load("Random_forest_model (2).pkl")

model_columns = [
    'num_occupants', 'house_size_sqft', 'monthly_income', 'outside_temp_celsius',
    'year', 'month', 'day', 'season',
    'heating_type_Electric', 'heating_type_Gas', 'heating_type_None',
    'cooling_type_AC', 'cooling_type_Fan', 'cooling_type_None',
    'manual_override_Y', 'manual_override_N',
    'is_weekend', 'temp_above_avg', 'income_per_person', 'square_feet_per_person',
    'high_income_flag', 'low_temp_flag',
    'season_spring', 'season_summer', 'season_fall', 'season_winter',
    'day_of_week_0', 'day_of_week_6', 'energy_star_home'
]

# Input form
with st.form("user_inputs"):
    st.header("📝 Enter Input Data")
    col1, col2 = st.columns(2)
    with col1:
        num_occupants = st.number_input("Occupants", min_value=1, value=3)
        house_size = st.number_input("House Size (sqft)", 100, 10000, value=1500)
        income = st.number_input("Monthly Income", 1000, 100000, value=40000)
        temp = st.number_input("Outside Temp (°C)", value=22.0)
    with col2:
        date = st.date_input("Date", value=datetime.date.today())
        heating = st.selectbox("Heating Type", ["Electric", "Gas", "None"])
        cooling = st.selectbox("Cooling Type", ["AC", "Fan", "None"])
        manual = st.radio("Manual Override", ["Yes", "No"])
        energy_star = st.checkbox("Energy Star Certified Home")
    submitted = st.form_submit_button("🔮 Predict")

if submitted:
    day_of_week = date.weekday()
    season_label = {12: 'winter', 1: 'winter', 2: 'winter',
                    3: 'spring', 4: 'spring', 5: 'spring',
                    6: 'summer', 7: 'summer', 8: 'summer'}.get(date.month, 'fall')

    features = {
        'num_occupants': num_occupants,
        'house_size_sqft': house_size,
        'monthly_income': income,
        'outside_temp_celsius': temp,
        'year': date.year,
        'month': date.month,
        'day': date.day,
        'season': {'spring': 2, 'summer': 3, 'fall': 4, 'winter': 1}[season_label],
        'heating_type_Electric': heating == "Electric",
        'heating_type_Gas': heating == "Gas",
        'heating_type_None': heating == "None",
        'cooling_type_AC': cooling == "AC",
        'cooling_type_Fan': cooling == "Fan",
        'cooling_type_None': cooling == "None",
        'manual_override_Y': manual == "Yes",
        'manual_override_N': manual == "No",
        'is_weekend': day_of_week >= 5,
        'temp_above_avg': temp > 22,
        'income_per_person': income / num_occupants,
        'square_feet_per_person': house_size / num_occupants,
        'high_income_flag': income > 40000,
        'low_temp_flag': temp < 15,
        'season_spring': season_label == "spring",
        'season_summer': season_label == "summer",
        'season_fall': season_label == "fall",
        'season_winter': season_label == "winter",
        'day_of_week_0': day_of_week == 0,
        'day_of_week_6': day_of_week == 6,
        'energy_star_home': energy_star
    }

    df = pd.DataFrame([{col: features.get(col, 0) for col in model_columns}])

    try:
        prediction = model.predict(df)[0]
        st.success(f"🔋 Estimated Energy Usage: *{prediction:.2f} kWh*")

        # Data for charts
        labels = ["Occupants", "House Size", "Income", "Outside Temp"]
        values = [num_occupants, house_size, income, temp]

        # Bar Chart
        fig_bar = go.Figure(go.Bar(
            x=values,
            y=labels,
            orientation='h',
            marker_color='lightskyblue'
        ))
        fig_bar.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0, r=0, t=30, b=0),
            yaxis=dict(tickfont=dict(color='white', size=14)),
            xaxis=dict(showticklabels=False)
        )

        st.subheader("📊 Bar Chart")
        st.plotly_chart(fig_bar, use_container_width=True)

        # Pie Chart (Donut)
        fig_pie = go.Figure(go.Pie(
            labels=labels,
            values=values,
            hole=0.4,
            marker_colors=['#636EFA', '#EF553B', '#00CC96', '#AB63FA'],
            textinfo='label+percent',
            textfont=dict(color='white', size=14)
        ))
        fig_pie.update_layout(
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(t=10, b=10, l=10, r=10)
        )

        st.subheader("🥧 Pie Chart")
        st.plotly_chart(fig_pie, use_container_width=True)

        # Line Chart
        # Simulate some trend data — example: energy usage over 7 days (dummy)
        days = [f"Day {i+1}" for i in range(7)]
        energy_usage = [prediction * (0.8 + 0.1 * i) for i in range(7)]  # rising trend

        fig_line = go.Figure(go.Scatter(
            x=days,
            y=energy_usage,
            mode='lines+markers',
            line=dict(color='deepskyblue', width=3),
            marker=dict(size=8)
        ))
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
```
