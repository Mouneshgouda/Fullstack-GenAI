```python
import os
import requests
import gradio as gr
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools

# 🌤️ Weather summary template
PROMPT_TEMPLATE = """
You are a weather analyst. Based on real-time weather in **{location}**, write a detailed weather report:

### 1. Current Weather
- Temperature: {temperature}°C
- Wind Speed: {windspeed} km/h
- Humidity: {humidity}%
- Sky: {description}

### 2. Recommendations
- What should a person wear?
- Precautions to take based on weather?

### 3. Patient-Friendly Insight
Explain the weather conditions in simple terms and how it affects daily life.

### 4. Add 2–3 helpful weather websites using DuckDuckGo.
"""

# Open-Meteo weather code meanings
WEATHER_CODES = {
    0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Rime fog", 51: "Light drizzle", 53: "Moderate drizzle",
    61: "Light rain", 63: "Moderate rain", 65: "Heavy rain",
    71: "Light snow", 73: "Moderate snow", 75: "Heavy snow",
    80: "Rain showers", 81: "Heavy rain showers",
    95: "Thunderstorm", 99: "Severe thunderstorm"
}

# 🌍 Get coordinates for a city
def get_coords(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    res = requests.get(url).json()
    if res.get("results"):
        return res["results"][0]["latitude"], res["results"][0]["longitude"]
    return None, None

# 🌦️ Get weather data from Open-Meteo
def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,windspeed_10m,weathercode&timezone=auto"
    return requests.get(url).json().get("current", {})

# 🔍 Weather Analysis Function
def analyze_weather(api_key, city):
    if not api_key:
        return "❌ Google API Key is missing."
    if not city.strip():
        return "❌ Please enter a valid city name."

    try:
        lat, lon = get_coords(city)
        if not lat:
            return "❌ City not found."

        weather = get_weather(lat, lon)
        desc = WEATHER_CODES.get(weather.get("weathercode", 0), "Unknown")

        # Format prompt
        prompt = PROMPT_TEMPLATE.format(
            location=city.title(),
            temperature=weather.get("temperature_2m", "N/A"),
            windspeed=weather.get("windspeed_10m", "N/A"),
            humidity=weather.get("relative_humidity_2m", "N/A"),
            description=desc
        )

        agent = Agent(
            model=Gemini(id="gemini-1.5-flash", api_key=api_key),
            tools=[DuckDuckGoTools()],
            markdown=True
        )

        return agent.run(prompt).content

    except Exception as e:
        return f"❌ Error: {e}"

# 🚀 Gradio App UI
with gr.Blocks() as demo:
    gr.Markdown("## 🌦️ AI Weather Reporter")
    gr.Markdown("Get live weather updates + AI analysis (powered by Open-Meteo + Gemini)\n⚠️ For demo use only.")

    api_key = gr.Textbox(label="🔐 Google API Key", type="password")
    city_name = gr.Textbox(label="📍 City Name", placeholder="e.g., Bengaluru, London")
    analyze_btn = gr.Button("🔍 Analyze Weather")
    output = gr.Markdown()

    analyze_btn.click(analyze_weather, inputs=[api_key, city_name], outputs=output)

demo.launch()
```


