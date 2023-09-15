import pandas as pd
import matplotlib.pyplot as plt

df_tesla = pd.read_csv('files/TESLA Search Trend vs Price.csv')

df_btc_search = pd.read_csv('files/Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('files/Daily Bitcoin Price.csv')

df_unemployment = pd.read_csv('files/UE Benefits Search vs UE Rate 2004-19.csv')

# What are the shapes of the DataFrames?
print(df_tesla.count())
print(df_unemployment.count())

# How many rows & columns do they have?
print(df_tesla.shape)
print(df_unemployment.shape)