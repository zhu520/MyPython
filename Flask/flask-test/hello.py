from flask import Flask
from flask import abort, redirect, url_for, render_template

app = Flask(__name__)

@app.errorhandler(401)
def page_not_found(error):
	return render_template('page_not_found.html'), 404

@app.route('/')
def index():
	return redirect(url_for('login'))

@app.route('/login')
def login():
	abort(401)
	this_is_never_executed()