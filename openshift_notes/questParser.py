from utils import Question
import commands
import pandas as pd 

df = pd.read_csv('data.csv')

questions = [
    Question(df['Question'][i], df['Answer'][i]) for i in range(len(df))
]

