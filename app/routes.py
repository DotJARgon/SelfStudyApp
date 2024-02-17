from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')
@app.route('/review')
def review():
    return render_template('review.html')
@app.route('/download')
def download():
    return render_template('download.html')