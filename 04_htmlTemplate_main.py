__author__ = 'Varun'
from flask import Flask, render_template

app = Flask(__name__)

# profile page - passing name variable into profile.html template in templates directory
@app.route('/profile/<name>') # GET, POST method
def profile(name):
    return render_template("profile.html",name=name)

if __name__ == "__main__":
    app.run(debug=True)
