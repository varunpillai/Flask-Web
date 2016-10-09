__author__ = 'Varun'
from flask import Flask, request

app = Flask(__name__)

# main page
@app.route('/') # GET method
def index():
    return 'Method used: %s' % request.method

#bacon page
@app.route('/bacon',methods=['GET','POST']) # GET, POST method
def bacon():
    if request.method == 'POST':
        return 'You are using %s' % request.method
    else:
        return 'You using: %s' % request.method

if __name__ == "__main__":
    app.run(debug=True)
