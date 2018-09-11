from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'
    return 'It's nice to meet you!'



@app.route('/goodbye_world')
def goodbye_world():
    return 'goodbye, World!'
