
from selenium import webdriver
import time

username='weiwei'
password='weiwei07'
home_url = 'https://parabank.parasoft.com/parabank/index.htm'
chromedriver='/Users/weiweiweng/Documents/Dev/selenium_banking/chromedriver'

#navigate to the website
driver= webdriver.Chrome(chromedriver)
driver.implicitly_wait(20)
driver.get(home_url) 

#enter username and password
username_field = driver.find_element_by_xpath("//input[@name='username']")
password_field = driver.find_element_by_xpath("//input[@name='password']")

username_field.send_keys(username)
password_field.send_keys(password)
time.sleep(5)

#to click login button
click_button= driver.find_element_by_xpath("//input[@class='button']")
click_button.click()

