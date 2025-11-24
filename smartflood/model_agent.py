import google.generativeai as genai
from .utils import log_actions


class FloodAgent:

    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def assess(self, risk_level, rainfall_avg, location):
        prompt = f"""
        You are a flood risk management AI assistant.

        Rainfall Analysis:
        - Location: {location}
        - Average rainfall: {rainfall_avg} mm

        Risk Level: {risk_level}
        - Give the name of the place and surrounding place based on given latitude and logitude 
        Based on agentic reasoning, provide:
        - Risk explanation
        - Recommended safety steps
        - If severe, suggest immediate alerts

        Keep the tone actionable and public-friendly.
        """

        response = self.model.generate_content(prompt)
        log_actions(f"Generated recommendation for {location} with risk={risk_level}")

        return response.text
