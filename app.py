from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def timer():
    return '\n'.join(('<head>',datetime.now().time().strftime('%H:%M:%S'),'</head>'))

app.run()



