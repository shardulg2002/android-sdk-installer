# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")
new_df = netflix_df[(netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] <= 1999) & (netflix_df['genre'] == 'Action')]

short_movie_count = 0

for label, row in new_df.iterrows():
    if row["duration"] < 90:
        short_movie_count = short_movie_count + 1
    else:
        short_movie_count = short_movie_count

print(short_movie_count)