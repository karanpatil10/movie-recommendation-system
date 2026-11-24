import streamlit as st
import pickle
import pandas as pd
import requests

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TMDB_API_KEY")

if not api_key:
    raise ValueError("TMDB_API_KEY is missing. Check your .env file.")

def fetch_poster(movie_id):
    response = requestes.get(.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = final_movies[final_movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recomended_movies_poster = []
    for i in movies_list:
        movie_id = i[0]
        
        recommended_movies.append(final_movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies

similarity = pickle.load(open('similarity.pkl','rb'))
movie_dict = pickle.load(open('movie_dict.pkl','rb'))
final_movies = pd.DataFrame(movie_dict)

st.title('Movie Recommendation System')

selected_movie = st.selectbox(
    "Your favourite movies",
    final_movies['title'].values
)


if st.button('Recommend'):
    recomendatations = recommended(selected_movie)
    for i in recomendatations:
        st.write(i)
