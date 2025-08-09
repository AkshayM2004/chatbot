from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # <-- This enables CORS for all routes

COLLEGE_INFO = {
    "admissions": "Admissions open in June every year. Contact admissions@xyzcollege.edu.",
    "library": "The library is open from 8 AM to 8 PM, Monday to Saturday.",
    "hod_cs": "Dr. A. Kumar is the Head of the Department for Computer Science."
}

@app.route('/info', methods=['GET'])
def get_info():
    topic = request.args.get('topic', '').lower()
    if topic in COLLEGE_INFO:
        return jsonify({"response": COLLEGE_INFO[topic]})
    else:
        return jsonify({"response": "Sorry, I don't have information on that topic."}), 404

if __name__ == "__main__":
    app.run(debug=True)
