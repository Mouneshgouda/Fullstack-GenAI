```python 

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

```
```python
## Background Image
 Clean & Minimal:
White-Gray Texture
https://images.unsplash.com/photo-1581287059658-4bfa556645b7

Paper Style
https://images.unsplash.com/photo-1542291026-7eec264c27ff

Concrete Wall
https://images.unsplash.com/photo-1548777123-e216912df019

 Nature Inspired:
Forest
https://images.unsplash.com/photo-1501785888041-af3ef285b470

Sky & Mountains
https://images.unsplash.com/photo-1507525428034-b723cf961d3e

Ocean
https://images.unsplash.com/photo-1506744038136-46273834b3fb

Technology/Abstract:
Futuristic Grid
https://images.unsplash.com/photo-1544197150-b99a580bb7a8

Cables / Data
https://images.unsplash.com/photo-1518770660439-4636190af475

Code in background
https://images.unsplash.com/photo-1581092580495-4c835cf5f92b

```python



```python
model_columns=[
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

```
