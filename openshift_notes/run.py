import os
from flask import Flask, render_template, request, redirect, flash, url_for, session

app = Flask(__name__)

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
		return redirect(url_for('user', usr=user))
	else:
		return render_template('login.html')


@app.route('/<usr>')
def user(usr):
	return f"<h1>{usr}</h1>"


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


