import selenium
from selenium import webdriver
from getpass import getpass
from time import sleep


use = "9928686241"
pwd = ""
#message=input('Enter your message for status:')



browser = webdriver.Chrome('/home/sunil/Downloads/chromedriver_linux64(1)/chromedriver')
browser.get('https://www.facebook.com/login')


username_box = browser.find_element_by_id('email')
username_box.send_keys(use)
sleep(3)


pwd_box=browser.find_element_by_id('pass')
pwd_box.send_keys(pwd)
sleep(3)


fb_login=browser.find_element_by_id('loginbutton')
fb_login.submit()
sleep(3)

#text_box =browser.find_element_by_xpath("//textarea[@name='xhpc_message']")
#text_box.send_keys(message)
#sleep(3)

#post_bt=browser.find_element_by_xpath("//button[contains(.,'Share')]")
#post_bt.click()
#print("post done")
