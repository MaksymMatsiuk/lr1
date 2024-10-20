from flask import Flask, jsonify
from service import get_greeting

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    greeting = get_greeting()
    return jsonify(greeting)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
