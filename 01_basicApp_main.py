__author__ = 'Varun'
from flask import Flask

app = Flask(__name__)

# main page
@app.route('/')
@app.route('/index')
def index():
    return 'This is the homepage'

# tuna page
@app.route('/tuna') # the address inside route is the path of the website
def tuna():
    return '<h2>Tuna is good</h2>'

#username page
@app.route('/profile/<username>')
def profile(username):
    return 'Hey there %s' %username

#post page
@app.route('/profile/<int:post_id>')
def post(post_id):
    return 'Post ID: %s' %post_id


if __name__ == "__main__":
    app.run(debug=True)
