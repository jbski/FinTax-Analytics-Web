from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/get_started')
def get_started():
    return render_template('get_started.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/subscribe')
def subcribe():
    return render_template('subscribe.html')


if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(debug=True)
