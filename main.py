from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    data = request.get_json()
    name = data.get('name', 'World')
    return jsonify({'message': f'Hello, {name}!'})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))