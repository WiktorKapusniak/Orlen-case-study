# Orlen-case-study

# Energy Trend Analyzer (LLM)

Automated system for analyzing industry trends in the energy sector using web scraping and Large Language Models (LLMs).

---

## Overview

This project automatically collects the latest articles from an energy-focused news portal and extracts structured insights such as:

* keywords
* sentiment
* main trend per article
* global trend across multiple articles

The goal is to demonstrate how AI can support market analysis and decision-making.

---

## Features

*  Web scraping using `requests` and `BeautifulSoup`
*  LLM-based analysis using OpenAI API
*  Extraction of structured data (JSON)
*  Identification of a global trend across articles
*  Fast and lightweight implementation

---

## Architecture

```
[News Website]
       ↓
[Python Scraper]
       ↓
[LLM Analysis]
       ↓
[Structured JSON Output]
       ↓
[Global Trend Detection]
```

---

## Tech Stack

* Python
* BeautifulSoup
* Requests
* OpenAI API
* JSON

---

## Example Output

```json
{
  "keywords": ["OZE", "energia"],
  "sentiment": "positive",
  "main_trend": "Growth of renewable energy investments"
}
```

### Global Trend

> Increasing investment in renewable energy as a response to energy market instability.

---

## Setup

### 1. Clone repository

```bash
git clone https://github.com/your-username/energy-trend-analyzer-llm.git
cd energy-trend-analyzer-llm
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set OpenAI API key

**Linux / Mac:**

```bash
export OPENAI_API_KEY="your_api_key"
```

**Windows (PowerShell):**

```powershell
setx OPENAI_API_KEY "your_api_key"
```

---

## Run

```bash
python main.py
```

---

## Key Insights

* Renewable energy is becoming a dominant trend
* Energy market instability (e.g. gas prices) influences investments
* AI enables fast and scalable analysis of industry trends

---

## Future Improvements

* Add more data sources (multiple websites)
* Real-time monitoring
* Visualization dashboard (e.g. Streamlit)
* More advanced NLP analysis

---

##  Author
**Wiktor Kapuśniak**

