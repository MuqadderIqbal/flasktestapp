from flask import Flask
#import pyttsx3 as ptx
app = Flask(__name__)

@app.route("/")
def index():
    #ptx.speak("Welcome")
    return "<h1> Hello World 123! </h1>"

if __name__ == "__main__":
    app.run(debug= True)

