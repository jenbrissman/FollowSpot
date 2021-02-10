from flask import Flask, jsonify, render_template, request
from model import connect_to_db,

app = Flask(__name__)


@app.route('/')
def homepage():
    """Show the homepage"""

    return render_template('index.html')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
