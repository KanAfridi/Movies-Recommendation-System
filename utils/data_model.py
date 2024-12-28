import gdown
import pickle

# Model file ID from Google Drive
MODEL_FILE_ID = '1JJb12M5kgOEsvwAmCNwgoV8YwFTmb8hh'
MODEL_NAME = 'recommendation_system.pkl'

# Download the model from Google Drive
gdown.download(f'https://drive.google.com/uc?id={MODEL_FILE_ID}', MODEL_NAME, quiet=False)


# Load the trained model and data from pickle files
def load_model():
    try:
        with open('recommendation_system.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("Model not found. Please train the model first.")
        return None

def load_data():
    try:
        with open('recommendation_data.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("data not found. Please train the model first.")
        return None
