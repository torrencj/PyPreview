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
    print("Starting display...")
    display = Display(visible=0, size=(1024,800))
    display.start()
    print("Loading site....")
    browser = webdriver.Chrome(executable_path='/app/.apt/usr/bin/google-chrome-stable') #Chromedriver is installed in a non default dir https://github.com/heroku/heroku-buildpack-xvfb-google-chrome
    browser.get('https://' + siteURL)
    browser.get_screenshot_as_base64('screenie.txt')
    return "Saved"

if __name__ == '__main__':
    app.run(debug=True)

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

display = Display(visible=0, size=(1024, 768))
display.start()
chrome_options = Options()
chrome_options.binary_location = '/app/.apt/opt/google/chrome/chrome'
driver = webdriver.Chrome('/app/.chromedriver/bin/chromedriver', chrome_options=chrome_options)

browser.get('http://www.ubuntu.com/')
print(browser.page_source)

browser.close()
display.stop()