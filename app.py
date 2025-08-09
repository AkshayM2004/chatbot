import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

COLLEGE_INFO = {
    "admissions": "Admissions open in June every year. Contact admissions@xyzcollege.edu.",
    "library": "The library is open from 8 AM to 8 PM, Monday to Saturday.",
    "hod_cs": "Dr. A. Kumar is the Head of the Department for Computer Science."
}

@app.route('/')
def home():
    return "Flask app is running!"

@app.route('/info', methods=['GET'])
def get_info():
    topic = request.args.get('topic', '').lower()
    if topic in COLLEGE_INFO:
        return jsonify({"response": COLLEGE_INFO[topic]})
    else:
        return jsonify({"response": "Sorry, I don't have information on that topic."}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
