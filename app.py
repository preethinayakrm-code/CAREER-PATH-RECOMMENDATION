from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load model and label encoder
with open('career_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('label_encoder.pkl', 'rb') as f:
    le = pickle.load(f)

CAREER_INFO = {
    "Data Science": {
        "icon": "🧠",
        "desc": "Uncover insights from data using statistics, ML, and storytelling.",
        "skills": ["Python", "Statistics", "Machine Learning", "Data Visualization"],
        "salary": "₹6L – ₹25L/yr",
        "growth": "Very High"
    },
    "Data Analytics": {
        "icon": "📊",
        "desc": "Turn raw data into actionable business decisions using analytics tools.",
        "skills": ["SQL", "Excel", "Tableau/Power BI", "Business Acumen"],
        "salary": "₹4L – ₹18L/yr",
        "growth": "High"
    },
    "Web Development": {
        "icon": "🌐",
        "desc": "Build and maintain websites and web apps for the modern internet.",
        "skills": ["HTML/CSS", "JavaScript", "React/Node.js", "Databases"],
        "salary": "₹4L – ₹20L/yr",
        "growth": "High"
    },
    "UI/UX": {
        "icon": "🎨",
        "desc": "Design intuitive, beautiful interfaces people love to use.",
        "skills": ["Figma", "User Research", "Prototyping", "Design Thinking"],
        "salary": "₹4L – ₹18L/yr",
        "growth": "High"
    },
    "Cybersecurity": {
        "icon": "🔐",
        "desc": "Protect systems, networks, and data from digital threats.",
        "skills": ["Networking", "Ethical Hacking", "Linux", "Cryptography"],
        "salary": "₹5L – ₹22L/yr",
        "growth": "Very High"
    },
    "Cloud Computing": {
        "icon": "☁️",
        "desc": "Design and manage scalable cloud infrastructure for modern apps.",
        "skills": ["AWS/Azure/GCP", "DevOps", "Linux", "Networking"],
        "salary": "₹6L – ₹24L/yr",
        "growth": "Very High"
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [
        float(data['programming']),
        float(data['communication']),
        float(data['creativity']),
        float(data['problem_solving']),
        float(data['ui_ux_interest']),
        float(data['ai_interest']),
        float(data['business_interest']),
    ]
    arr = np.array([features])
    probs = model.predict_proba(arr)[0]
    top3_idx = np.argsort(probs)[::-1][:3]
    results = []
    for idx in top3_idx:
        career = le.classes_[idx]
        info = CAREER_INFO.get(career, {})
        results.append({
            "career": career,
            "confidence": round(float(probs[idx]) * 100, 1),
            "icon": info.get("icon", "💼"),
            "desc": info.get("desc", ""),
            "skills": info.get("skills", []),
            "salary": info.get("salary", ""),
            "growth": info.get("growth", "")
        })
    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)
