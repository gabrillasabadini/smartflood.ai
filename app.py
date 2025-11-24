import streamlit as st
from dotenv import load_dotenv
import os

from smartflood.data_fetcher import WeatherFetcher
from smartflood.utils import calculate_risk
from smartflood.model_agent import FloodAgent


st.title("🌧️ SmartFlood AI: Real-time Disaster Awareness System")


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ GEMINI_API_KEY missing. Create .env file first.")
    st.stop()

lat = st.number_input("Enter Latitude", value=19.0760)
lon = st.number_input("Enter Longitude", value=72.8777)

if st.button("Analyze Flood Risk"):
    st.info("Fetching live weather data...")

    fetcher = WeatherFetcher()
    precipitation = fetcher.fetch_rain_data(lat, lon)

    risk_level, avg_rain = calculate_risk(precipitation)

    st.write(f"**Average rainfall:** {avg_rain:.2f} mm")
    st.write(f"**Risk Category:** 🚨 {risk_level}")

    agent = FloodAgent(api_key)
    with st.spinner("AI reasoning in progress..."):
        suggestion = agent.assess(risk_level, avg_rain, f"{lat},{lon}")

    st.success("AI Assessment Ready:")
    st.write(suggestion)


st.divider()
st.caption("Powered by Public API + Gemini Reasoning + Streamlit")
