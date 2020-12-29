import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object("config.DevelopmentConfig")
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return jsonify({
        'data':'Hello World'
    })

@app.route('/<name>')
def hello_name(name):
    return jsonify(
        data=name
    )

if __name__ == '__main__':
    app.run(port=8080)