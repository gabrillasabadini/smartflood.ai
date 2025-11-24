# smartflood.ai

# 📘 SmartFlood AI — Agentic Disaster Risk Assistant

SmartFlood AI is a **hands-on educational project** designed to demonstrate how **Agentic AI workflows** can interact with **real-world public data**, reason autonomously using **LLMs (Gemini)**, and produce actionable insights using a **Streamlit web interface**.

This project helps learners understand:

* How AI agents interact with external systems.
* How to integrate a Large Language Model into an application.
* How decision-making pipelines work (data → reasoning → recommendations).
* How to build and deploy a working AI-powered application end-to-end.

---

## 🚀 Project Purpose

This system simulates how an AI agent could support **flood risk assessment and public alert systems**.

It:

🔹 Fetches **live rainfall data** from the free **Open-Meteo Public Weather API**
🔹 Computes rainfall averages and classifies **risk severity (Low/Medium/High)**
🔹 Uses **Gemini LLM reasoning** to generate **location-specific safety analysis**
🔹 Logs decisions for reproducibility — mimicking **agent memory**
🔹 Provides a clean **Streamlit dashboard**

---

## 🧰 Features Overview

| Feature                 | Description                                  |
| ----------------------- | -------------------------------------------- |
| 🌦 Live data fetch      | Real-time precipitation using Open-Meteo API |
| 🧠 Agentic AI reasoning | Gemini model generates contextual insights   |
| 🔍 Risk classification  | Automates hazard mapping based on rainfall   |
| 🗂 Logging system       | Saves every generated decision               |
| 🖥️ Streamlit App       | Interactive dashboard for end users          |

---

## 🏗️ System Architecture

```
Public Weather API --> Data Fetcher --> Risk Engine --> Agentic AI (Gemini)
                                                    ↓
                                              Streamlit App
                                                    ↓
                                              Decision Log
```

---

## 📁 Folder Structure

```
SmartFlood-AI/
│
├── smartflood/
│   ├── __init__.py
│   ├── data_fetcher.py
│   ├── model_agent.py
│   ├── utils.py
│
├── streamlit_app.py
├── requirements.txt
├── README.md
├── logs.txt (auto-created after running)
└── .env (created by user, not included in repo)
```

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Project

```sh
git clone https://github.com/YOUR_USERNAME/SmartFlood-AI.git
cd SmartFlood-AI
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Add Environment Variables

Create a `.env` file in the root folder:

```
GEMINI_API_KEY=YOUR_GEMINI_KEY_HERE
```

> 🔑 You can obtain a Gemini key from: [https://ai.google.dev](https://ai.google.dev)

---

## ▶️ Running the Application

```sh
streamlit run streamlit_app.py
```

Once launched, enter:

* **Latitude**
* **Longitude**

Then press **Analyze Flood Risk**.

Example useful coordinates:

| Location            | Latitude | Longitude |
| ------------------- | -------- | --------- |
| Mumbai, India       | 19.0760  | 72.8777   |
| Houston, USA        | 29.7604  | -95.3698  |
| Manila, Philippines | 14.5995  | 120.9842  |

---

## 📊 How Risk is Calculated

The system averages rainfall from the last 24–48 hours and classifies risk:

| Average Rainfall (mm) | Risk Level |
| --------------------- | ---------- |
| 0 – 5 mm              | Low        |
| 5 – 20 mm             | Medium     |
| > 20 mm               | High       |

---

## 🤖 AI Agent Behavior

Once the risk level is determined, Gemini is prompted to generate:

* A short risk explanation
* Recommended actions
* If needed — **urgent evacuation messaging**

Example response:

> “Rainfall averages indicate rising flood pressure. Residents should avoid waterlogged areas, secure valuables, and stay tuned for local authority updates.”

All generated results are stored in:

```
logs.txt
```

This simulates **agent memory for auditability**.

---

## 🧑‍🏫 Teaching Notes: Learning Outcomes

Learners will understand:

| Topic                       | Demonstrated Through               |
| --------------------------- | ---------------------------------- |
| REST API usage              | `data_fetcher.py`                  |
| AI agent workflow           | `model_agent.py`                   |
| Application logic           | `utils.py`                         |
| Frontend interaction        | `streamlit_app.py`                 |
| LLM prompting & engineering | Custom reasoning-prompt chain      |
| Deployment best practices   | Requirements file + Env management |

---
---

## 🛡 License

This project is provided for **educational and prototyping purposes only**.
Not certified for real-world disaster response.

---

## ✨ Acknowledgments

| Source            | Usage                            |
| ----------------- | -------------------------------- |
| Open-Meteo API    | Real-time weather data           |
| Google Gemini API | AI reasoning and recommendations |
| Streamlit         | UI framework                     |

---

## 👤 Author / Instructor Notes

You can use this project in:

* Classroom workshops
* AI pipeline demonstrations
* Hackathons
* Capstone project starter templates
* Agentic AI engineering lessons

