from flask import Flask
from flask import render_template

app = Flask(__name__)
app.run(debug=True)

dd = [
    'dddd',
    'ddd',
    'dd',
    'd',
]

@app.route("/")
def hello():  
    return render_template('index.html',dd=dd)

@app.route("/aa/<xxx>")
def aa(xxx):
    return render_template('index.html', xxx=xxx)