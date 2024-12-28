import pandas as pd
import pickle 
import streamlit as st
from api_poster import fetch_images
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.data_model import load_data, load_model

        
# call the function 
data = load_data()
similarity_model = load_model()

# Recommend similar movies based on the given movie title and id to fetch the poster 
def movies_similarity(title): 
    """
    This function uses a pre-trained similarity model to find movies that are
    most similar to the provided title. It retrieves the movie titles and their 
    corresponding posters for the top 5 most similar movies.

    Example:
    recommended_titles, recommended_posters = movies_similarity("Inception")
    """
    try:
        recommended_movies = []
        recommended_movies_poster = []
        indx = data[data['title'] ==  title].index
        similar_array = similarity_model[indx][0]
        fivesimilar_movies= sorted(list(enumerate(similar_array)), reverse = True, key = lambda x: x[1])[1:6]
        
        for i, score in fivesimilar_movies:
            movies_title = data.iloc[i]['title']
            movies_ids = data.iloc[i]['id']
            images_path = fetch_images(movies_ids)
            
            recommended_movies.append(movies_title)
            recommended_movies_poster.append(images_path)
        return recommended_movies, recommended_movies_poster
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None


# Display the title of the app and select the movie to get recommendations
st.title("Movies Recommendation system")
selected_movies = st.selectbox('Enter your favorite movie', data['title'])

# To predict the recommendations of your favorite movies displayy the poster of the movies 
if st.button('Recommendation'):
        title, posters = movies_similarity(selected_movies)
        st.subheader("Recommended Movies:")
        for i in title:
            
            col1, col2, col3, col4, col5 = st.columns(5) # , col6, col7
        with col1:
            st.markdown(f"#### {title[0]}")  # Use H3 for smaller text
            st.image(posters[0])

        with col2:
            st.markdown(f"#### {title[1]}") 
            st.image(posters[1])

        with col3:
            st.markdown(f"#### {title[2]}")  
            st.image(posters[2])

        with col4:
            st.markdown(f"#### {title[3]}") 
            st.image(posters[3])

        with col5:
            st.markdown(f"#### {title[4]}") 
            st.image(posters[4])


