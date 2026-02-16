from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/v1/messages', methods=['POST'])
@app.route('/v1/v1/messages', methods=['POST'])
def proxy_messages():
    resp = requests.post('http://localhost:1234/v1/chat/completions', 
                        json=request.json)
    return jsonify(resp.json())

if __name__ == '__main__':
    app.run(port=8000)