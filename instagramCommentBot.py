from pynput.keyboard import Key, Controller
from selenium import webdriver
import chromedriver_binary
import time

# Creates Keyboard Controller
keyboard = Controller()

# open browser
browser = webdriver.Chrome()
browser.get('https://www.instagram.com/')
time.sleep(5)

# Input Username of Secondary Account
emailElem = browser.find_element_by_name("username")
emailElem.send_keys('USERNAME/EMAIL')

# Input Password of Secondary Account
passElem = browser.find_element_by_name("password")
passElem.send_keys('PASSWORD')
time.sleep(2)
passElem.submit()
time.sleep(10)

# Open Post Link
browser.get('POST LINK')

# List Of Comments
comments = ['LIST OF COMMENTS','IN THIS FORMAT']
time.sleep(5)

# Loop Through Comments to Post
for x in comments:
    # Gets and Clicks the Comment Section
    element = browser.find_element_by_class_name('Ypffh')
    element.click()
    time.sleep(2)    
    # Types Comment
    keyboard.type(x)
    # Checks if Still Clicked
    element = browser.find_element_by_class_name('Ypffh')
    element.click()
    time.sleep(2)
    # Triple Checks if Comment was Posted
    for count in range(3):
        element = browser.find_element_by_class_name('Ypffh')
        keyboard.press(Key.enter)
        # Helps with Spam Detection
        time.sleep(2)
        element.click()
        time.sleep(1)
    # Helps with Comment Errors
    time.sleep(5)