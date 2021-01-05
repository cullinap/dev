import os
import json
from flask import Flask, render_template, request, redirect, flash, url_for, session
from datetime import timedelta
import sqlalchemy
from helpers import Quiz, match_page_info_with_url


app = Flask(__name__)
app.secret_key = "temp_key" # set the secret key 
quiz_data = 'data/quiz_data.json'

quiz = Quiz("username")
QUESTIONS = 2


'''
-when login it goes to the first question
-html
	-jinja
		-remove it/comment it out
	-html
	-python code
		-check score & url

'''

# routing
# view
# logic
# route resolution


# set home screen

@app.route('/')
def login():
	if request.method == 'POST':
		username = request.form['username'].strip()
		return redirect(url_for('quiz_app'))

	return render_template('index.html')


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

	def get_url(self):
		return self.url # return the current url

	def get_score(self):
		return self.score # return the current score

	def get_question_asked(self):
		return str(self.url) # same as get url? 

	def correct_answer(self):
		self.url += 1 # if correct go to next question
		self.score += 1 # if correct add one point

	def wrong_answer(self):
		self.score -= 1 # if wrong subtract a point

quiz = Quiz() # create an instance of Quiz named quiz

# define a route listening at /home and execute a fn named home
# accept the GET and POST HTTP methods
@app.route('/home', methods=['GET','POST'])
def home(): #view function
	quiz.score = 0 # if we go back home score resets to 0
	quiz.url = 1 # url resets to 1
	return render_template('home.html') # serve the home template

@app.route('/vmd_timestamp', methods=['GET','POST'])
def vmd_timestamp():
	# get url from data, pass current url from quiz instance
	question = match_question_with_url(quiz.get_url())  
	score = str(quiz.get_score()) # get the current score 
	# render a template with this info
	return render_template('/vmd_timestamp.html', question=question, score=score)

@app.route('/terminal', methods=['GET','POST'])
def terminal():
	# get url from data, pass current url from quiz instance
	question = match_question_with_url(quiz.get_url())  
	score = str(quiz.get_score()) # get the current score 
	# render a template with this info
	return render_template('/terminal.html', question=question, score=score)

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
		else:
			quiz.wrong_answer() # decrement score
			# POTENTIALLY REDUNDANT? 
			redirect(url_for('vmd_timestamp')) # redirect to quiz page

	return redirect(url_for('vmd_timestamp'))

# controls a home button to return well...home
@app.route('/button', methods=['POST'])
def button():
	if request.method == 'POST':
		return redirect(url_for('home'))
	# if request.method == 'POST':
	# 	return redirect(url_for('home'))








################## OLD STUFF ########################



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


@app.route('/final_score')
def final_score():
	riddle = match_page_info_with_url(quiz_data, quiz.get_url())
	user = session['user']
	final_score = 0 #final_tally_message(quiz.get_score(), quiz.get_url())
	flash(f'final score {final_score}')
	return render_template('member.html', riddle=riddle, user=user)


@app.route('/logout') # logout page
def logout():
	flash("You have been logged out", "info")
	session.pop("user", None) # remove curent user session name
	quiz.Score = 0
	#session['url'] = 0
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


