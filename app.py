import streamlit as st
import pickle 
import requests
import streamlit.components.v1 as components
from PIL import Image
from feedback import *
#******************************************************************************************#

def fetch(movie_id):
    path='https://api.themoviedb.org/3/movie/{}?api_key=39c53de430ca9c4663b9376d4c16d715'.format(movie_id)
    r=requests.get(path)
    r=r.json()
    poster_path=r['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

#******************************************************************************************#

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommand_mov=[]
    recommend_poster=[]
    for i in distance[1:12]:
        movies_id=movies.iloc[i[0]].id
        recommand_mov.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch(movies_id))

    return recommand_mov,recommend_poster

#******************************************************************************************#

# image = Image.open('netflix.png')
# st.image(image)
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("netflix.png")

with col3:
    st.write(' ')

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:
    st.write(" ")

with col3:
    st.write(' ')
imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")
imageUrls = [
    fetch(429617),
    fetch(370665),
    fetch(841755),
    fetch(558),
    fetch(24428),
    fetch(100402),
    fetch(10757),
    fetch(155),
    fetch(598),
    fetch(914),
    fetch(255709),
    fetch(572154)
     ]
imageCarouselComponent(imageUrls=imageUrls, height=200)


#******************************************************************************************#


st.header("Movie Recommender System")
movies = pickle.load(open( "movies_list.pkl" , "rb"))
similarity=pickle.load(open("similarity.pkl","rb"))

movies_list=movies['title'].values
selectvalue=st.selectbox("Select Movies from dropdown",movies_list)

if st.button("Show Recommend"):
    movie_name,movie_poster=recommend(selectvalue)
    col1,col2,col3,col4,col5=st.columns(5,gap="large")
    col6,col7,col8,col9,col10=st.columns(5,gap="large")

    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
    with col6:
        st.text(movie_name[5])
        st.image(movie_poster[5])
    with col7:
        st.text(movie_name[6])
        st.image(movie_poster[6])
    with col8:
        st.text(movie_name[7])
        st.image(movie_poster[7])
    with col9:
        st.text(movie_name[8])
        st.image(movie_poster[8])
    with col10:
        st.text(movie_name[9])
        st.image(movie_poster[9])

if st.button("Give Feedback"):
    st.markdown("[Click here to go to the link](nmrfeedbackform.streamlit.app)")



