import base64
from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
import os
import json
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Instill API Token from .env file
INSTILL_API_TOKEN = os.getenv("INSTILL_API_TOKEN")
API_URL = "https://api.instill.tech/v1beta/users/manulthanura/pipelines/tailormyresume/trigger"

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
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

        # Log the full API response
        # print("API Response:", response_data) 

        if response.status_code == 200:
            api_response = response.json()
            
            # Extract the outputs list
            outputs = api_response.get('outputs', [])
            
            if outputs:
                # Extract the resume evaluation from the first output
                resume_evaluation = outputs[0].get('resume_evaluation', '')
                
                if resume_evaluation:
                    # Parse the JSON string from 'resume_evaluation'
                    evaluation_data = json.loads(resume_evaluation)
                    
                    # Extract individual values
                    resume_rating = evaluation_data.get('Resume Rating')
                    total_skills = evaluation_data.get('Total Skills')
                    experience = evaluation_data.get('Experience')
                    rejection_probability = evaluation_data.get('Rejection Probability')
                    areas_meeting_requirements = evaluation_data.get('Areas Meeting Requirements', [])
                    areas_for_improvement = evaluation_data.get('Areas for Improvement', [])
                    
                    # Render the result on the page
                    return render_template(
                        'results.html',
                        resume_rating=resume_rating,
                        total_skills=total_skills,
                        experience=experience,
                        rejection_probability=rejection_probability,
                        areas_meeting_requirements=areas_meeting_requirements,
                        areas_for_improvement=areas_for_improvement
                    )
                else:
                    return render_template('results.html', error="No evaluation available")
            else:
                return render_template('results.html', error="No outputs received from API")



    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
