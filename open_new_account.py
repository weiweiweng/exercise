
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.select import Select

username='weiwei'
password='weiwei07'
home_url = 'https://parabank.parasoft.com/parabank/index.htm'
chromedriver='/Users/weiweiweng/Documents/Dev/selenium_banking/chromedriver'

#navigate to the website
driver= webdriver.Chrome(chromedriver)
driver.implicitly_wait(20)
driver.get(home_url) 

#enter username and password,login
username_field = driver.find_element_by_xpath("//input[@name='username']")
password_field = driver.find_element_by_xpath("//input[@name='password']")

username_field.send_keys(username)
password_field.send_keys(password)
time.sleep(5)
#to click login button
click_button= driver.find_element_by_xpath("//input[@class='button']")
click_button.click()


#open new account
wbwait = WebDriverWait(driver,20)
open_new_account = wbwait.until(EC.presence_of_element_located((By.LINK_TEXT,"Open New Account")))
open_new_account.click()
print(driver.title)
print('create new account page opened')

#select from drop down account
account_type = driver.find_element(By.XPATH,"//select[@id='type']")
select_account_type = Select(account_type)
select_account_type.select_by_visible_text('SAVINGS')
print('account type is selected')
time.sleep(10)

account_number = driver.find_element(By.XPATH,"//select[@id='fromAccountId']")
select_account_number = Select(account_number)
select_account_number.select_by_index(0)
print('account number is selected')

driver.find_element(By.XPATH, "//input[@class='button' and @value='Open New Account']").click()
print('account is created')

time.sleep(5)
title_msg = wbwait.until(EC.presence_of_element_located((By.XPATH, "//h1[@class='title']")))
title_msg.text
assert "Account Opened!" in title_msg.text
