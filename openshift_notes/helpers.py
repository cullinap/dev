import json



def match_page_info_with_url(json_file, number):
	riddle = {}
	with open(json_file, "r") as json_data:
		data = json.load(json_data)
		for obj in data:
			if obj['url'] == str(number):
				riddle = obj

	return riddle 

class Quiz(object):
	def __init__(self, username):
		#self.username = username
		self.score = 0
		self.url = 1
		self.username = username

	def get_url(self):
		return self.url

	def get_score(self):
		return self.score

	def get_questions_asked(self):
		return str(self.url - 1)

	def correct_answer(self):
		self.url += 1
		self.score += 1

	def pass_question(self):
		self.url += 1

def final_tally_message(score, url):
	message = ""
	if url > 2:
		if score == 0:
			message = "Wow real bad dude"
		elif score == 1:
			message = "Meh"
		else:
			message = "Pro"
	return message 