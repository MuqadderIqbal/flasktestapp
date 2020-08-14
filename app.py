from flask import Flask
from random import choice
import requests

#import pyttsx3 as ptx
app = Flask(__name__)

def get_random_joke(joke_category = None):
    available_joke_categories = ["general", "programming", "knock-knock"]
    random_jokes_api = "https://official-joke-api.appspot.com/jokes/{0}/random"
    if not(joke_category) or str.lower(joke_category) not in available_joke_categories:
        joke_category = choice(available_joke_categories) #"general"
    joke_url = random_jokes_api.format(joke_category)
    print("Joke URL:" , joke_url)
    joke_resp_json = requests.get(joke_url).json()[0]
    joke_type = joke_resp_json.get("type")
    joke_setup = joke_resp_json.get("setup")
    joke_punchline = joke_resp_json.get("punchline")
    return (joke_type, joke_setup, joke_punchline)

@app.route("/")
def index():
    _, joke_setup, joke_punchline = get_random_joke()
    html_str = "<h1> " + joke_setup +  " </h1>" + "<p>"
    html_str += "<h2> " + joke_punchline +  " </h2>" 
    return html_str

# @app.route("/joke")
# def get_joke(joke_category:str = None):
#     _, joke_setup, joke_punchline = get_random_joke()
#     html_str = "<h1> " + joke_setup +  " </h1>" + "<p>"
#     html_str += "<h2> " + joke_punchline +  " </h2>" 
#     return html_str

if __name__ == "__main__":
    app.run(debug= True)

