import os
from flask import Flask, render_template, request, redirect, flash, url_for, session

app = Flask(__name__)
app.secret_key = "temp_key"

# @app.route('/', methods=["GET","POST"])
# def login():
# 	if request.method == "POST":
# 		username = request.form['username'].strip()
# 		session['username'] = username
# 		session['score'] = 0
# 		session['url'] = 1
# 		return redirect('leaderboard')
# 	return render_template("index.html")

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/login', methods=['POST','GET'])
def login():
	if request.method == "POST":
		user = request.form['nm']
		session['user'] = user
		return redirect(url_for('user'))
	else:
		if 'user' in session:
			return redirect(url_for('user'))
			
		return render_template('login.html')

@app.route('/user')
def user():
	if "user" in session:
		user = session["user"]
		return f"<h1>{user}</h1>"
	else:
		return redirect(url_for('login'))

@app.route('/logout')
def logout():
	session.pop("user", None)
	return redirect(url_for('login'))


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


