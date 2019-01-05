from flask import Flask, flash, escape,redirect, render_template, request, session,url_for,jsonify, abort
from hashlib import md5

app = Flask(__name__)

@app.route('/')
def index():
    print 'index method  called'
    return render_template('demo.html')

if __name__ == '__main__':
    app.run()