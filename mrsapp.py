import pickle
import streamlit as st
import requests
import gdown


def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=681582bac9c222d3962e56dd0aa495a6"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except Exception as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Error"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_ = []
    recommended_movie_poster = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_poster.append(fetch_poster(movie_id))
        recommended_movie_.append(movies.iloc[i[0]].title)

    return recommended_movie_,recommended_movie_poster


st.header('Movie Recommender System')

url = "https://drive.google.com/uc?id=1OSqHeYQVEZTqQ55kLF_NymdK6Juph0No"  # replace with your ID
output = "similarity.pkl"
gdown.download(url, output, quiet=False)
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_,recommended_movie_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_[0])
        st.image(recommended_movie_poster[0])
    with col2:
        st.text(recommended_movie_[1])
        st.image(recommended_movie_poster[1])

    with col3:
        st.text(recommended_movie_[2])
        st.image(recommended_movie_poster[2])
    with col4:
        st.text(recommended_movie_[3])
        st.image(recommended_movie_poster[3])
    with col5:
        st.text(recommended_movie_[4])
        st.image(recommended_movie_poster[4])
