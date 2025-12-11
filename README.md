# SNS Comment Sentiment Analysis Tool (FastAPI × Python)

This is a simple yet functional **sentiment analysis web application** built with **FastAPI**.  
It evaluates text input (such as comments from Twitter, Radiotalk, YouTube, etc.) and classifies the sentiment as:

- **Positive**
- **Negative**
- **Neutral**

The project is designed to demonstrate the fundamentals of building modern web applications with FastAPI, Python, and Jinja2 templates.

---

## 🚀 Demo Overview

When launching the application locally, users can:

- Enter any text comment
- Submit the form
- View sentiment results  
  → classification label, score, and detected positive/negative keywords

---

## ✨ Features

### ✔ Sentiment Classification
- Dictionary-based scoring  
- Detects matched positive and negative keywords  
- Displays overall sentiment score and category

### ✔ Simple & Clean Web UI
Built using:
- **FastAPI** for backend processing
- **Jinja2** for template rendering

### ✔ Beginner-Friendly Code Structure
Ideal for demonstrating FastAPI fundamentals and Python backend development skills.

---

## 📁 Project Structure

```
sns-sentiment-app/
│── main.py               # FastAPI application
│── sentiment.py          # Sentiment analysis logic
│── requirements.txt      # Python dependencies
│── README.md             # Documentation
└── templates/
    └── index.html        # Frontend template
```

---

## 🧠 Tech Stack

| Technology | Description |
|------------|-------------|
| **Python 3.10+** | Programming language |
| **FastAPI** | Modern, high-performance web framework |
| **Jinja2** | Template engine for HTML rendering |
| **Uvicorn** | ASGI server to run FastAPI applications |

---

## 🖥️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/MinoruAshikari/sns-sentiment-app.git
cd sns-sentiment-app
```

### 2. (Optional) Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the development server

```bash
uvicorn main:app --reload
```

Open the app in your browser:

👉 http://127.0.0.1:8000

---

## 📝 Future Improvements (Roadmap)

- Integrate machine learning models (BERT, Transformers)
- Add Japanese language tokenization (MeCab / Sudachi)
- Support external APIs (YouTube API, Radiotalk API)
- Deploy with Docker
- Host on Render / Vercel / Heroku for public access
- Add a richer sentiment dictionary or use ML-based scoring

---

## 👤 Author

**Minoru Ashikari**

- Aspiring AI & Python developer  
- Building practical tools with FastAPI and Python  
- Based in Malaysia  
- Creator, podcaster, and digital content producer  

---

## ⭐️ Support

If you find this project useful, please consider giving the repository a **Star ⭐**.  
Your support encourages further development and learning!
