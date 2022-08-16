import  streamlit as st
import pandas as pd
import pickle
import requests

def recommend(movie):
    movie_index = movies[movies['MovieName'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].MovieName)
    return recommended_movies


movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movies['MovieName'].values
st.title("Movie Recommendation system")

selected_movie_name = st.selectbox(
    'Select a movie',
    movies_list
)

if st.button('Get Recommendations'):
    recommendations = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    col_list = [col1, col2, col3, col4, col5]
    x =0
    for i in recommendations:
        poster_path_idx = movies[movies["MovieName"] == i].index
        poster_path = movies.loc[poster_path_idx]["Poster_Path"].tolist()[0]
        poster = requests.get(poster_path)
        col_list[x].image(poster.content)
        col_list[x].write(i)
        x = x + 1



