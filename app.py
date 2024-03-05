from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
    {
        "id": 1,
        "title": "Data Scientist",
        "location": "Delhi, India",
        "salary": "15,00,000"
    },
    {
        "id": 2,
        "title": "Data Analyst",
        "location": "Bengaluru, India",
        "salary": "10,00,000"
    },
    {
        "id": 3,
        "title": "DevOps Engineer",
        "location": "Remote",
        "salary": "10,00,000"
    }
]
@app.route('/')
def home():
    return render_template('index.html', jobs=jobs, company_name="Career Pathways")

@app.route('/api/jobs')
def api_route():
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)