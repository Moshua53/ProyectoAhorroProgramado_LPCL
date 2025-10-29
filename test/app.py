
from flask import Flask

from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("ahorro.html")

if __name__ == '__main__':
    app.run( debug=True )