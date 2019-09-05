from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

@app.route('/sum/<int:a>/<int:b>')
def get_sum(a,b):
	return '{} + {} = {}'.format(a,b,a+b)

@app.route('/<username>')
def show_username(username):
	return username

@app.route('/projects/')
def projects():
	return 'The project page'

@app.route('/about')
def about():
	return 'The about page'

@app.route('/user/<username>')
def show_user_profile(username):
	return 'User {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post {}'.format(post_id)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
	return 'Subpath {}'.format(subpath)

@app.route('/')
def index():
	#return 'Index Page'
	return render_template('hello.html')

@app.route('/hello')
def hello_world():
    return 'Hello, World!'
