from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


url = "https://parabank.parasoft.com/parabank/index.htm"
username = "weiwei"
password = "weiwei07"
chromedriver = "/Users/weiweiweng/Documents/Dev/selenium_banking/chromedriver"

info= {'Firstname':'Wei','Lastname': 'We', 'Street': '8703 19th Ave', 'City': 'Brooklyn', 
    'State': 'NY', 'Zipcode': '11214', 'Phone':'9178687812','Username':'weiwei','Password':'weiwei07','SSN':'12345678'}



driver = webdriver.Chrome(chromedriver)
driver.implicitly_wait(10)
driver.get(url)

# driver.find_elements_by_link_text('Register').click()
driver.find_element(By.LINK_TEXT, 'Register').click()

#expilicity wait.per situation
Webwait= WebDriverWait(driver,20)
first_name = Webwait.until(EC.presence_of_element_located((By.ID,'customer.firstName')))
last_name = Webwait.until(EC.presence_of_element_located((By.ID,'customer.lastName')))


first_name.send_keys(info['Firstname'])
last_name.send_keys(info['Lastname'])
driver.find_element(By.ID,'customer.address.street').send_keys(info['Street'])
driver.find_element(By.ID,'customer.address.city').send_keys(info['City'])
driver.find_element(By.ID,'customer.address.state').send_keys(info['State'])
driver.find_element(By.ID,'customer.address.zipCode').send_keys(info['Zipcode'])
driver.find_element(By.ID,'customer.phoneNumber').send_keys(info['Phone'])
driver.find_element(By.ID,'customer.ssn').send_keys(info['SSN'])
driver.find_element(By.ID,'customer.username').send_keys(info['Username'])
driver.find_element(By.ID,'customer.password').send_keys(info['Password'])
driver.find_element(By.ID,'repeatedPassword').send_keys(info['Password'])

driver.find_element(By.XPATH,"//table[@class='form2']//input[@class='button']").click()

print(driver.title)
assert 'Customer Created ' in driver.title
driver.quit()



