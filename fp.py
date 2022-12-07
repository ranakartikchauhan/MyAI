# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask ,render_template, request
from main import myfun
import pywhatkit as kit
import wikipedia
import pyttsx3
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

def search_on_google(query):
    kit.search(query)

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(text):
    """Used to speak whatever text is passed to it"""
    engine.say(text)
    engine.runAndWait()
	

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	# a=input("Please Enter what you want serach : ")
	# search_on_google(a)
	# return render_template('index.html')
	return render_template('student.html')
@app.route("/wiki")
def mywiki():
	a=input("Please Enter what you want serach : ")
	rr=search_on_wikipedia(a)
	gg=speak(rr)
	return gg
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)
	

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
