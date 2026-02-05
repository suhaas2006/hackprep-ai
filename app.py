from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 HackPrep AI Backend - You.com API integration coming soon!"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    challenge = data.get('challenge', 'You.com APIs')
    skills = data.get('skills', 'Python solo student')
    
    # You.com API will replace this mock response
    return jsonify({
        "title": "HackPrep AI",
        "tech": "Flask + You.com API + HTML/JS", 
        "timeline": "Day 1-2: MVP, Day 3-16: Polish + Deploy",
        "next_steps": "Connect You.com API, add PDF export"
    })

if __name__ == '__main__':
    app.run(debug=True)
