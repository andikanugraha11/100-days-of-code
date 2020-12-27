from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        'data':'Hello World'
    })

app.run(port=8080)