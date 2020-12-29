import pandas as pd 
import datetime as dt
import random

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        
def run_test(questions):
    score = 0
    random_question = random.randint(0,1)
    if random_question == 1:
        print('random question!')
        val = random.randint(0,8)
        answer = input(questions[val].prompt + "\n")
        if answer == questions[val].answer:
            print('good job')
        else:
            print('you are a failure')

    else: 
        for question in questions:
            answer = input("\n" + question.prompt + "\n")
            if answer == question.answer:
                score += 1
        print(f'\n\tYou got {score}/{len(questions)} correct')

        with open('score.txt', 'a+') as file_object:
            now = dt.datetime.now()
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write('\n')
            file_object.write(str(now) + ": " + str(score))


# get average for day and print that 

# plot a graph of progress to see how I am doing

# 