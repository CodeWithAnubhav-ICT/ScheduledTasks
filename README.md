# 🌦️ Automated Rain-Alert System

A serverless Python application that monitors local weather forecasts and sends automated SMS alerts if rain is predicted, deployed entirely infrastructure-free using GitHub Actions.

## 🚀 Overview

This project was built as part of the **100 Days of Code** challenge (Day 35). The script fetches a 5-day weather forecast every 3 hours for specified geographic coordinates, parses the hourly weather condition codes, and alerts the user via SMS if rain or storms are expected during the day.

### The Problem & The Pivot
Traditional tutorials for this project rely on external hosting platforms like PythonAnywhere for scheduling. Due to platform limitation updates removing scheduled tasks from the free tier, this project adapts by utilizing **GitHub Actions** as a cron scheduler. This provides a resilient, zero-cost, and entirely cloud-native deployment pipeline.

---

## 🛠️ Features & Architecture

* **Weather API Integration:** Interacts with the OpenWeatherMap API to retrieve high-resolution JSON weather forecast payloads.
* **SMS Gateway:** Utilizes the Twilio API to dispatch immediate SMS alerts with dynamic, context-aware emojis.
* **CI/CD Automation:** Deployed via a GitHub Actions workflow that executes the runtime script on a automated daily cron schedule.
* **Secure Secret Management:** Fully decoupled configuration using secure environment variables (`os.environ`) to protect sensitive API tokens and proxy configurations.

---

## 📦 Infrastructure & Engineering Takeaways

Using public GitHub Actions runners for task scheduling offers an incredible, zero-infrastructure alternative for lightweight automation scripts. 

**Cloud Constraint Insight:** Public GitHub runner cron tasks operate on a best-effort queue. During peak global traffic times, scheduled jobs can experience execution delays of 2–3 hours. For a daily weather alert where minute-level precision is non-critical, it stands as an exceptionally efficient, serverless approach to automation.

---

## 🔧 Setup & Configuration

To deploy this script yourself, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/CodeWithAnubhav-ICT/Rain-Alert-System.git](https://github.com/CodeWithAnubhav-ICT/RainAlert.git)
   cd RainAlert
