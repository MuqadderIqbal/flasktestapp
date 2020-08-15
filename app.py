from flask import Flask
from funcs import get_random_joke

#import pyttsx3 as ptx
app = Flask(__name__)



@app.route("/")
def index():
    _, joke_setup, joke_punchline = get_random_joke()
    html_str = "<h1> " + joke_setup +  " </h1>" + "<p>"
    html_str += "<h2> " + joke_punchline +  " </h2>" 
    return html_str

# @app.route("/joke")


if __name__ == "__main__":
    app.run(debug= True)

