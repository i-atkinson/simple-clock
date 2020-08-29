from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/timer')
def timer():
    time_str=datetime.now().time().strftime('%H:%M:%S')
    return jsonify({"time":time_str})

app.run()



