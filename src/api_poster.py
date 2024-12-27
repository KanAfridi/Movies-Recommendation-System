import requests
import os 
import sys

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)
# The function to fetch movies poster from api
def fetch_images(movie_id = None):
    try:
        # API details
        api_key = "2d93afa4fe9bcb72ba4e36370e670b79"
        language = "en-US"

        # Construct the URL
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/images"

        # Make the API request
        insert_id_inUrl = url.format(movie_id = movie_id)
        response = requests.get(insert_id_inUrl, params={"api_key": api_key})

        # Handle the response
        if response.status_code == 200:
            data = response.json()
            poster = data['posters'][0]
            poster_file_path = poster['file_path']
            Full_image_url = f"https://image.tmdb.org/t/p/w500/{poster_file_path}" 
            return Full_image_url
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
        return None