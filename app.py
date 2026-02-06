from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head><title>HackPrep AI</title>
    <style>body{font-family:sans-serif;max-width:800px;margin:50px auto;padding:20px;background:#f5f5f5}
    input,button{padding:12px;font-size:16px;width:100%;margin:10px 0}
    #output{padding:20px;background:white;border-radius:8px;margin-top:20px}
    .powered-by{color:#666;font-size:14px}
    .result {line-height:1.6}
    .loading {color:#888; font-style:italic}</style>
    </head>
    <body>
        <h1>🚀 HackPrep AI</h1>
        <p>You.com-powered hackathon project planner</p>
        <input id="input" placeholder="Enter: You.com APIs + Python solo student + 16 days">
        <button onclick="generate()">Generate Plan</button>
        <div id="output">Click button to see magic ✨</div>
        <div class="powered-by">Powered by You.com APIs | DeveloperWeek 2026</div>
        <script>
        async function generate(){
            document.getElementById('output').innerHTML = '<div class="loading">🔄 Connecting to backend...</div>';
            try {
                const input = document.getElementById('input').value;
                const response = await fetch('/generate', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({challenge: input})
                });
                const data = await response.json();
                document.getElementById('output').innerHTML = `
                    <div class="result">
                        <h3>🎯 Hackathon Project Plan</h3>
                        <p><strong>🚀 Title:</strong> ${data.title}</p>
                        <p><strong>💻 Tech Stack:</strong> ${data.tech}</p>
                        <p><strong>⏱️ Timeline:</strong> ${data.timeline}</p>
                        <p><strong>📈 Impact:</strong> ${data.impact}</p>
                    </div>
                `;
            } catch(error) {
                document.getElementById('output').innerHTML = '<div style="color:#e74c3c">⚠️ Backend error - check terminal</div>';
            }
        }
        </script>
    </body>
    </html>
    '''

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    challenge = data.get('challenge', 'generic hackathon')
    
    # Mock AI response (You.com API coming next)
    response = {
        "title": f"AI Hackathon Planner for {challenge}",
        "tech": "Flask + You.com API + HTML/CSS/JS + Render.com",
        "timeline": "Day 1: MVP → Day 2: Deploy → Day 3-16: Polish",
        "impact": "Saves 10+ hours planning, 90% submission rate boost"
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

