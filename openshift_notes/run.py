import os
import json
from datetime import datetime
import pandas as pd
from flask import Flask, render_template, request, redirect, flash, url_for, session
from datetime import timedelta
import sqlalchemy
from helpers import Quiz, match_page_info_with_url


app = Flask(__name__)
app.secret_key = "temp_key" # set the secret key 
quiz_data = 'data/quiz_data.json'
quiz = Quiz("username")
QUESTIONS = 2

# # set home screen
# @app.route('/')
# def login():
# 	if request.method == 'POST':
# 		username = request.form['username'].strip()
# 		return redirect(url_for('quiz_app'))

# 	return render_template('index.html')


def match_question_with_url(number):
	# function returns question based on int provided
	question = {} # load question in a set
	with open ('./data/quiz_data.json', 'r') as json_data: #json I/O
		testData = json.load(json_data) # create the iterable
		for obj in testData: # loop though each question obj
			if obj['url'] == str(number): # if the obj url matches the int input
				question = obj # set the question value to that obj

	return question

# getting an answer to match with question
# most likely redundant, but can move later
def match_answer_with_url(number):
	answer = {}
	with open ('./data/quiz_data.json', 'r') as json_data:
		testData = json.load(json_data)
		for obj in testData:
			if obj['url'] == str(number):
				answer = obj

	return answer['answer'] # same as above just return answer 

# Quiz obj to store score, url, and updates 
# essentially tracks and records current state of game
class Quiz(object):
	def __init__(self):
		self.url = 1 # start the game at question/url 1
		self.score = 0 # start with a score of zero
		self.attempt = 0
		self.total_attempts = 0
		self.hint = False

	def get_url(self):
		return self.url # return the current url

	def get_score(self):
		return self.score # return the current score

	def get_attempt(self):
		return self.attempt 

	def total_attempts(self):
		return self.total_attempts 

	def get_question_asked(self):
		return str(self.url) # same as get url? 

	def get_hint_status(self):
		return self.hint

	def skip_question(self):
		self.url += 1 
		self.attempt = 0

	def correct_answer(self):
		self.url += 1 # if correct go to next question
		self.score += 1 # if correct add one point
		self.attempt = 0
		self.total_attempts += 1

	def wrong_answer(self):
		self.score -= 1 # if wrong subtract a point
		self.attempt += 1
		self.total_attempts += 1
		self.hint = True


quiz = Quiz() # create an instance of Quiz named quiz

# define a route listening at /home and execute a fn named home
# accept the GET and POST HTTP methods
@app.route('/', methods=['GET','POST'])
def home(): #view function
	if request.method == "POST":
		for key, value in request.form.items():
			print(f'{key}: {value}')

		session['user'] = request.form['user']

		quiz.score = 0 # if we go back home score resets to 0
		quiz.url = 1 # url resets to 1
		quiz.attempt = 0
		quiz.total_attempts = 0
		return redirect(url_for('terminal'))

	return render_template('home.html')  
		#return redirect(url_for('home'))
		#return render_template('home.html') # serve the home template
	# else:
	# 	return render_template('home.html') 

# @app.route('/vmd_timestamp', methods=['GET','POST'])
# def vmd_timestamp():
# 	# get url from data, pass current url from quiz instance
# 	question = match_question_with_url(quiz.get_url())  
# 	score = str(quiz.get_score()) # get the current score 
# 	# render a template with this info
# 	return render_template('/vmd_timestamp.html', question=question, score=score)

@app.route('/terminal', methods=['GET','POST'])
def terminal():
	render_template('/add_stock.html')
	if quiz.url > 1:
		return redirect(url_for('final_score'))


	# get url from data, pass current url from quiz instance
	question = match_question_with_url(quiz.get_url())  
	score = str(quiz.get_score()) # get the current score 
	#render a template with this info





	return render_template('/terminal.html', question=question, score=score)

	#default hint status set to false, if there is a wrong answer and 2 attempts there will be a hint
	# HINT is set to the question json from the current url and hint is loaded into jinja
	HINT = ""
	if quiz.get_hint_status() and quiz.get_attempt() >= 2:
		HINT = question
		return render_template('/terminal.html', question=question, score=score, hint=HINT)



# 6 Jan 20: also added in main question/sub question into json

# controls answer submissino 
@app.route('/submit_data', methods=['POST'])
def submit_data():
	question = match_question_with_url(quiz.get_url()) # get current question
	score = str(quiz.get_score()) # get current score
	if request.method == 'POST': # if I press the button
		req = request.form # fetch info from form posted
		answer = req.get('answer') # get username from form and set it to answer
		# * POTENTIONALLY REDUNDANT * with question var above
		if answer == match_answer_with_url(quiz.get_url()): # get answer from json
			quiz.correct_answer() # increement question score and url state
		elif quiz.attempt == 3:  # check the attempts in the quiz class and if eq to 3 skip the question
			quiz.skip_question()
		else:
			quiz.wrong_answer() # decrement score
			# POTENTIALLY REDUNDANT? 
			redirect(url_for('terminal')) # redirect to quiz page

	return redirect(url_for('terminal'))

# controls a home button to return well...home
@app.route('/button', methods=['POST'])
def button():
	if request.method == 'POST':
		return redirect(url_for('home'))
	# if request.method == 'POST':
	# 	return redirect(url_for('home'))

@app.route('/final_score')
def final_score():
	riddle = match_page_info_with_url(quiz_data, quiz.get_url())
	final_score = quiz.get_score()
	total_attempts = quiz.total_attempts
	date_and_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	user = session["user"]
	with open('./data/data.txt', 'a') as file_object:
		file_object.write(str(user) + (": ") + str(date_and_time) + (": ") + str(final_score) + (" ") + str(total_attempts) + '\n')

	#user = session['user']
	#final_score = 0 #final_tally_message(quiz.get_score(), quiz.get_url())
	flash(f'final score {final_score}')
	quiz.score = 0 # if we go back home score resets to 0
	quiz.url = 1 # url resets to 1
	quiz.attempt = 0
	quiz.total_attempts = 0

	return render_template('member.html', riddle=riddle, score=final_score)


################## OLD STUFF ########################

@app.route("/add_stock", methods=['GET','POST'])
def add_stock():
	if request.method == 'POST':
		for key, value in request.form.items():
			print(f'{key} {value}')

		session['stock_symbol'] = request.form['stock_symbol']
		session['number_of_shares'] = request.form['number_of_shares']
		session['purchase_price'] = request.form['purchase_price']
		return redirect(url_for('list_stocks'))

	return render_template('add_stock.html')

@app.route('/stocks/')
def list_stocks():
	return render_template('stocks.html')
 




@app.route('/quiz', methods=['GET','POST'])
def quiz_app():
	if request.method == 'POST':
		total = quiz.get_questions_asked()
		riddle = match_page_info_with_url(quiz_data, quiz.get_url())
	# 	if quiz.get_url() > QUESTIONS:
	# 		return redirect('leaderboard')


	return render_template('member.html', user=quiz, riddle=riddle, total=total)


@app.route('/submit_answer', methods=['POST'])
def submit_answer():
	riddle = match_page_info_with_url(quiz_data, quiz.get_url())
	if request.method == 'POST':
		guess = request.form['answer'].strip().title()
		answer = riddle['answer']
		if quiz.get_url() < QUESTIONS:
			if guess == answer:
				quiz.correct_answer()

		elif quiz.get_url() == QUESTIONS:
			if guess == answer:
				quiz.correct_answer()
				
				return redirect(url_for('final_score'))
				
	#return render_template('member.html', riddle=riddle, user=user, total=total)
	return redirect(url_for('quiz_app'))


# @app.route('/final_score')
# def final_score():
# 	riddle = match_page_info_with_url(quiz_data, quiz.get_url())
# 	final_score = quiz.get_score()
# 	#user = session['user']
# 	#final_score = 0 #final_tally_message(quiz.get_score(), quiz.get_url())
# 	flash(f'final score {final_score}')
# 	return render_template('member.html', riddle=riddle, score=final_score)


@app.route('/logout') # logout page
def logout():
	flash("You have been logged out", "info")
	session.pop("user", None) # remove curent user session name
	quiz.Score = 0
	#session['url'] = 0
	return redirect(url_for('/')) # got back to the login page


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


