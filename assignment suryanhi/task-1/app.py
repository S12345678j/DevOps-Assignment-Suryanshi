from flask import Flask, jsonify, request, render_template
from database import init_db, get_messages, add_message

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# === API Endpoints ===

@app.route('/api/messages', methods=['GET'])
def api_get_messages():
    messages = get_messages()
    return jsonify(messages)

@app.route('/api/messages', methods=['POST'])
def api_add_message():
    data = request.get_json()
    content = data.get('content')
    if content:
        add_message(content)
        return jsonify({'status': 'success'}), 201
    return jsonify({'error': 'No content provided'}), 400

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
