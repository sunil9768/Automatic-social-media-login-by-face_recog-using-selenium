import selenium
from selenium import webdriver
from getpass import getpass
from time import sleep


use = "9928686241"
pwd = "********"
#message=input('Enter your message for status:')



browser = webdriver.Chrome('/home/sunil/Downloads/chromedriver_linux64(1)/chromedriver')
browser.get('https://in.linkedin.com/')


username_box = browser.find_element_by_id('login-email')
username_box.send_keys(use)
sleep(3)


pwd_box=browser.find_element_by_id('login-password')
pwd_box.send_keys(pwd)
sleep(3)


fb_login=browser.find_element_by_id('login-submit')
fb_login.submit()
sleep(3)


