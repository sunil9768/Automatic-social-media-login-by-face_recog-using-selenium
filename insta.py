from selenium import webdriver
from random import randint
import time
from selenium.webdriver.common.by import By


browser= webdriver.Chrome("/home/sunil/Downloads/chromedriver_linux64(1)/chromedriver")
browser.get("https://www.instagram.com/accounts/login/")
time.sleep(8) #time.sleep count can be changed depending on the Internet speed.

#Fill username value
username_field = browser.find_element_by_name('username')
username_field.send_keys("9928686341")

#Fill password value
password_field  = browser.find_element_by_name('password')
password_field.send_keys("********") 

post_bt=browser.find_element_by_xpath("//button[contains(.,'Log in')]")
post_bt.click()
print("done")
time.sleep(8)


