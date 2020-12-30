import os
import json
from flask import Flask, render_template, request, redirect, flash, url_for, session
from datetime import timedelta
import sqlalchemy


app = Flask(__name__)
app.secret_key = "temp_key" # set the secret key 
app.permanent_session_lifetime = timedelta(days=300) # establish session lifetime
quiz_data = 'data/quiz_data.json'


# @app.route('/', methods=["GET","POST"])
# def login():
# 	if request.method == "POST":
# 		username = request.form['username'].strip()
# 		session['username'] = username
# 		session['score'] = 0
# 		session['url'] = 1
# 		return redirect('leaderboard')
# 	return render_template("index.html")

# set home screen
@app.route('/')
def home():
	return render_template('index.html')

# set login screen get=unsecure post=secure
@app.route('/login', methods=['POST','GET'])
def login():
	if request.method == "POST": # check if we reached page with POST request, if POST take name info 
		session.permanent = True # set permanent session
		user = request.form['nm'] # take data from login.html form 
		session['user'] = user # set the session user name to name from request form
		session['url'] = 2
		flash("Login Successful!")
		return redirect(url_for('quiz_app')) # go to user page with session info
	else:
		if 'user' in session:
			session['url'] = 1
			flash("Already logged in!")
			return redirect(url_for('quiz_app')) # if you already logged in

		return render_template('login.html') # if method not post go back to login


def match_page_info_with_url(json_file, number):
	riddle = {}
	with open(json_file, "r") as json_data:
		data = json.load(json_data)
		for obj in data:
			if obj['url'] == str(number):
				riddle = obj

	return riddle 


@app.route('/quiz')
def quiz_app():
	total = session['url'] - 1
	session['url'] = 1
	user = session["user"]
	with open(quiz_data, "r") as json_data:
		data = json.load(json_data)
		for obj in data:
			riddle = obj


	#riddle = match_page_info_with_url(quiz_data, session['url'])

	return render_template('member.html', riddle=riddle, user=user, total=total)


# user page
@app.route('/user')
def user():
	if "user" in session: # check if the user is in session
		user = session["user"] # set the user variable to the value assoaciated with user session
		return f"<h1>{user}</h1>" # return a page showing the user's name
	else:
		flash("You are not logged in")
		return render_template("user.html", user=user)  # if user not in session go back to login

@app.route('/logout') # logout page
def logout():
	flash("You have been logged out", "info")
	session.pop("user", None) # remove curent user session name
	return redirect(url_for('login')) # got back to the login page


# @app.route('/')
# def index():
# 	return render_template("index.html")

# @app.route('/leaderboard')
# def leaderboard():
#     return render_template("leaderboard.html")
    
# @app.route('/riddles')
# def riddles():
#     return render_template("riddles.html")

if __name__ == '__main__':
	app.run(debug=True)


