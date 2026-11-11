from flask import Flask, render_template, jsonify
import random

app = Flask(__name__, template_folder='.')

# Mock database of projects for your showcase
PROJECTS = [
    {
        "id": 1,
        "title": "E-Commerce Analytics Dashboard",
        "description": "A real-time data visualization tool tracking retail sales, user retention, and inventory turnover metrics.",
        "tech_stack": ["Python", "Flask", "React", "Tailwind CSS"]
    },
    {
        "id": 2,
        "title": "Smart Home Automation Hub",
        "description": "An IoT centralized controller platform managing connected lighting, security, and climate hardware ecosystems.",
        "tech_stack": ["Go", "MQTT", "Docker", "Vue.js"]
    },
    {
        "id": 3,
        "title": "AI Text Summarizer & Synthesizer",
        "description": "A natural language processing pipeline that condenses long-form documentation into actionable structured insights.",
        "tech_stack": ["Python", "PyTorch", "FastAPI", "Next.js"]
    }
]

@app.route('/')
def home():
    """Renders the main index page."""
    return render_template('index.html')

@app.route('/api/projects', methods=['GET'])
def get_projects():
    """API endpoint that returns a list of showcase projects."""
    return jsonify({
        "status": "success",
        "data": PROJECTS
    })

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """API endpoint generating dynamic metrics for visual flair."""
    return jsonify({
        "status": "success",
        "metrics": {
            "uptime": "99.98%",
            "active_users": random.randint(1200, 1500),
            "api_requests_24h": random.randint(45000, 50000)
        }
    })

if __name__ == '__main__':
    # Run the application locally in debug mode
    app.run(debug=True, port=5000)
