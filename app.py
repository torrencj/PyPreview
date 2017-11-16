#!flask/bin/python

from flask import Flask
from pyvirtualdisplay import Display
from selenium import webdriver

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/<siteURL>', methods=['GET'])
def get_pic(siteURL):
    # return "Hello " + siteURL
  display = Display(visible=0, size=(1024,800))
  display.start()
  print("Starting display...")
  browser = webdriver.Chrome("/app/.apt/usr/bin/google-chrome") #Chromedriver is installed in a non default dir https://github.com/heroku/heroku-buildpack-xvfb-google-chrome
  print("Loading site....")
  browser.get('https://' + siteURL)
  browser.get_screenshot_as_base64('screenie.txt')
  return "Saved"

if __name__ == '__main__':
    app.run(debug=True)
