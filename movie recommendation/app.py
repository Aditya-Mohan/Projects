import streamlit as st
import pickle
import requests
import numpy as np
import pandas as pd

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=358c3c5695eb3571ef2313386c6ab8fc&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index=moviess[moviess['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    reco=[]
    poster=[]
    for i in movies_list:
        movie_id=moviess.iloc[i[0]].movie_id
        reco.append(moviess.iloc[i[0]].title)
        poster.append(fetch_poster(movie_id))
    return reco,poster
#Loading Pickle
similarity=pickle.load(open('similarity.pkl','rb'))
moviess=pickle.load(open('movies.pkl','rb'))

# Generating List of Movie
moviesss=moviess['title'].values

#Title
st.title("Movie Recommendation System")
#Selectbox
selected=st.selectbox('What would you like to watch',moviesss)
#Button
if st.button('Recommend'):
    recommendation,poster=recommend(selected)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendation[0])
        st.image(poster[0])
    with col2:
        st.text(recommendation[1])
        st.image(poster[1])

    with col3:
        st.text(recommendation[2])
        st.image(poster[2])
    with col4:
        st.text(recommendation[3])
        st.image(poster[3])
    with col5:
        st.text(recommendation[4])
        st.image(poster[4])
