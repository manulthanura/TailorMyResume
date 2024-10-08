import base64
from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
import os
from dotenv import load_dotenv
import markdown  # Import the markdown library

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Instill API Token from .env file
INSTILL_API_TOKEN = os.getenv("INSTILL_API_TOKEN")
API_URL = "https://api.instill.tech/v1beta/users/manulthanura/pipelines/tailormyresume/trigger"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_resume():
    job_description = request.form.get('job_description')
    resume = request.files.get('resume')

    if not job_description or not resume:
        return jsonify({"error": "Please provide both job description and resume."}), 400

    # Read and encode the resume file as base64
    resume_content = resume.read()
    resume_base64 = base64.b64encode(resume_content).decode('utf-8')

    # Prepare the API request payload
    payload = {
        "inputs": [
            {
                "job_description": job_description,
                "resume_pdf_file": resume_base64
            }
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {INSTILL_API_TOKEN}"
    }

    # Send request to Instill API
    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response_data = response.json()

        if response.status_code == 200:
            # Extract feedback from API response
            evaluation = response_data['outputs'][0].get("resume_evaluation", "No evaluation available")
            skill_match = response_data['outputs'][0].get("resume_skill_match", "No skill match available")

            # Convert markdown to HTML
            evaluation_html = markdown.markdown(evaluation)
            skill_match_html = markdown.markdown(skill_match)

            # Render the results page with HTML content
            return render_template('results.html', evaluation=evaluation_html, skill_match=skill_match_html)

        else:
            return jsonify({"error": "Failed to process the resume", "details": response_data}), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
