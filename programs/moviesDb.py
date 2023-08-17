import pandas as pd

movie_dataframe = pd.read_csv("C:\LearningThings\PythonPandas\databases\popular_10000_movies_tmdb.csv")

print("our dataframe ...\n", movie_dataframe)

idrow = movie_dataframe.loc[:10, ['id']]

print(idrow)