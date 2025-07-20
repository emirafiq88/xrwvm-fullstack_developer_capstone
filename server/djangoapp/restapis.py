# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# In restapis.py

def get_request(endpoint, **kwargs):
    # TEST LINE: Add this print statement
    print("--- USING THE CORRECT restapis.py CODE ---")

    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"

    # URL FIX: Make sure the default is 3030
    backend_url = os.getenv(
        'backend_url', default="http://localhost:3030")

    # --- Corrected Code ---
    request_url = "http://localhost:3030" + endpoint + "?" + params

    print("GET from {} ".format(request_url))
    try:
        response = requests.get(request_url)
        return response.json()
    except:
        print("Network exception occurred")

# def analyze_review_sentiments(text):
def analyze_review_sentiments(text):
    # This line adds the missing "/" to the URL
    request_url = sentiment_analyzer_url + "/analyze/" + text
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return None # Return None on failure

# def post_review(data_dict):
def post_review(data_dict):
    # Use the correct URL for the Node.js server
    request_url = "http://localhost:3030/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        return response.json()
    except:
        print("Network exception occurred")
