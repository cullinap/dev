import os
from flask import Flask, render_template, request, redirect, flash, url_for, session
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "temp_key" # set the secret key 
app.permanent_session_lifetime = timedelta(days=300) # establish session lifetime

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
		flash("Login Successful!")
		return redirect(url_for('user')) # go to user page with session info
	else:
		if 'user' in session:
			flash("Already logged in!")
			return redirect(url_for('user')) # if you already logged in

		return render_template('login.html') # if method not post go back to login

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


