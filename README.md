# CareerCompass — Career Path Recommendation Website

A Flask web app powered by your trained Random Forest model.

## Project Structure
```
career_website/
├── app.py                  # Flask backend
├── career_model.pkl        # Your trained model
├── label_encoder.pkl       # Your label encoder
├── requirements.txt
└── templates/
    └── index.html          # Frontend UI
```

## Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

> ⚠️ Your model was trained with scikit-learn 1.6.1. Use the same version to avoid warnings.

### 2. Run the app
```bash
python app.py
```

### 3. Open in browser
Visit: http://127.0.0.1:5000

## Features
- 7 skill/interest sliders (matching your model's features exactly)
- Top 3 career recommendations with confidence scores
- Salary range & growth outlook for each career
- Animated match confidence bars
- Fully responsive dark UI

## Model Details
- **Algorithm:** Random Forest Classifier (200 trees)
- **Input Features:** Programming, Communication, Creativity, Problem Solving, UI/UX Interest, AI Interest, Business Interest
- **Output Classes:** Cloud Computing, Cybersecurity, Data Analytics, Data Science, UI/UX, Web Development

## Deploying Online (Optional)
You can deploy this for free on:
- **Render.com** — push to GitHub, connect repo, set start command: `python app.py`
- **Railway.app** — similar GitHub deploy flow
- **PythonAnywhere** — upload files manually, run Flask app
