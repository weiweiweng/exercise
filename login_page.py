from selenium import webdriver
import time


url = "https://parabank.parasoft.com/parabank/index.htm"
username = "weiwei"
password = "weiwei07"
chromedriver = "/Users/weiweiweng/Documents/Dev/selenium_banking/chromedriver"



#step1
#open browser, create an object for chromedriver to talk to chromebrowser

driver = webdriver.Chrome(chromedriver)
driver.maximize_window()

#navigating to the website
driver.get(url)

# get the title of the page
home_page_title = driver.title
print(home_page_title)


#locat4e username and password in the html document
usernamefield = driver.find_element_by_xpath("//input[@name='username']")
passwordfield = driver.find_element_by_xpath("//input[@name='password']")

#enter username and password
usernamefield.clear()
usernamefield.send_keys(username)
passwordfield.clear()
passwordfield.send_keys(password)

#click login
driver.find_element_by_xpath("//input[@class='button']").click()
account_page_title = driver.title
print(account_page_title)
time.sleep(5)
 

#find check balance by account number
account_number ='13899'
available_amount = f"//table/tbody/tr[@class='ng-scope']/td/a[contains(text(),'{account_number}')]/../../td[3]"
balance = driver.find_element_by_xpath(available_amount).text
print(balance)

# def check_balance(account_number):
#     available_amount = "//table/tbody/tr[@class='ng-scope']/td/a[contains(text(),'{account_number}')]/../../td[3]"
#     balance = driver.find_element_by_xpath(available_amount).text
#     return balance