from flask import render_template
from flask import send_from_directory
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/static/<path:path>')
def download_file(filename):
    return send_from_directory('static',filename)