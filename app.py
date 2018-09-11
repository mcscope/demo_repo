from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

#Inserted a comment here, Freddy
@app.route('/goodbye_world')
def goodbye_world():
    return 'goodbye, World!'
