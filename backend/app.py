from flask import Flask, request, jsonify
from flask_cors import CORS
from jd_parser import get_all_jobs, summarize_jd
from cv_parser import extract_cv_data
from matcher import match_score
from mailer import send_mail
import os

app = Flask(__name__)
CORS(app)

CV_FOLDER = '../CV'
MATCH_THRESHOLD = 60  # Lowered for better testing results

@app.route('/jobs', methods=['GET'])
def list_jobs():
    try:
        return jsonify(get_all_jobs())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/scan', methods=['POST'])
def scan_cvs():
    try:
        job_role = request.json.get('job')
        jd_summary = summarize_jd(job_role)
        shortlisted = []

        print(f"\n🔍 Scanning for job: {job_role}")
        print(f"📄 JD Summary:\n{jd_summary}")

        for file in os.listdir(CV_FOLDER):
            if file.endswith('.pdf'):
                path = os.path.join(CV_FOLDER, file)
                print(f"📄 Reading: {path}")

                cv_data = extract_cv_data(path)
                print(f"👤 Scanning {file} => {cv_data.get('name')} ({cv_data.get('email')})")

                score = match_score(jd_summary, cv_data)
                print(f"📊 Match Score: {score}%")

                if score >= MATCH_THRESHOLD:
                    send_mail(cv_data['email'], job_role)
                    shortlisted.append({'name': cv_data['name'], 'score': score})

        print(f"✅ Total shortlisted: {len(shortlisted)}")
        return jsonify({'shortlisted': shortlisted})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)