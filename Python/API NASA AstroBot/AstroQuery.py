# Importing necessary libraries
import requests  # I use this for making HTTP requests to external APIs.
import nltk  # NLTK is my choice for natural language processing in Python.
from nltk.corpus import stopwords  # Importing stopwords to filter out common words.
from nltk.tokenize import word_tokenize  # Tokenizer to break text into words.
from nltk import pos_tag  # Part-of-speech tagger to identify words' roles in sentences.

# Ensuring necessary NLTK datasets are downloaded
nltk.download('punkt')  # 'punkt' tokenizer models are essential for word tokenization.
nltk.download('averaged_perceptron_tagger')  # This is needed for part-of-speech tagging.
nltk.download('stopwords')  # Stopwords dataset is used to remove common, less meaningful words.

# Function to process user input and extract key information
def process_user_input(input_text):
    # I start by converting the input text to lowercase for consistency.
    tokens = word_tokenize(input_text.lower())
    # Next, I tag each token with its part of speech.
    tagged = pos_tag(tokens)

    # Extracting nouns to identify key subjects in the query
    nouns = [word for word, pos in tagged if pos.startswith('NN')]
    
    # I remove stopwords to focus on the most meaningful words.
    cleaned_nouns = [word for word in nouns if word not in stopwords.words('english')]
    return cleaned_nouns

# Function to choose the correct NASA API endpoint based on subjects
def fetch_nasa_data(api_key, query_subjects):
    # I initialize an empty dictionary to hold the data I fetch.
    data = {}
    # If 'mars' is a subject of interest, I fetch data from the Mars Rover Photos API.
    if 'mars' in query_subjects:
        url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={api_key}"
        # Storing the response in the 'data' dictionary under 'mars_photos'.
        data['mars_photos'] = requests.get(url).json()

    # Placeholder for fetching star or constellation data
    if 'star' in query_subjects or 'constellation' in query_subjects:
        data['star_info'] = "Star or constellation data functionality to be implemented."

    # Checking for interest in the Astronomy Picture of the Day.
    if 'picture' in query_subjects or 'astronomy' in query_subjects:
        url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
        # Storing the Astronomy Picture of the Day data.
        data['apod'] = requests.get(url).json()

    # Returning the fetched data.
    return data

# Demonstrating how to use the functions
user_input = "Show me pictures of stars and the Mars rover"
# Processing the user input to extract relevant subjects.
subjects = process_user_input(user_input)
api_key = 'MY_NASA_API_KEY'  # Replace this with your actual NASA API key.
# Fetching data from NASA based on the subjects extracted from user input.
nasa_data = fetch_nasa_data(api_key, subjects)
# Finally, I print out the data I fetched.
print(nasa_data)
