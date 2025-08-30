# first test with python in Github Web

# Libraries
import pandas as pd
import matplotlib as plt

url = "https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv"

df = pd.read_csv(url)

print(df.head())
