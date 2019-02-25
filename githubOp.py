import selenium
from selenium import webdriver
from getpass import getpass
from time import sleep


use = "8559931989"
pwd = "********"
#message=input('Enter your message for status:')



browser = webdriver.Chrome('/home/sunil/Downloads/chromedriver_linux64(1)/chromedriver')
browser.get('https://github.com/login')


username_box = browser.find_element_by_id('login_field')
username_box.send_keys(use)
sleep(3)


pwd_box=browser.find_element_by_id('password')
pwd_box.send_keys(pwd)
sleep(3)


github_login=browser.find_element_by_name('commit')
github_login.submit()
sleep(3)




