from utils import Question
from question_prompts import question_prompts
import commands
import pandas as pd 

df = pd.read_csv('data.csv')

questions = [
    Question(df['Question'][i], df['Answer'][i]) for i in range(len(df))
]

