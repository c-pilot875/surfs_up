from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hellow World'

export FLASK_APP=app.py
set FLASK_APP=app.py
Flask run