import os
from selenium import webdriver

chromedriver = "C:/Chromedriver/chromedriver.exe"    #path where chromedriver exists
os.environ["webdriver.chrome.driver"] = chromedriver 
driver = webdriver.Chrome(chromedriver)
driver.get("Any website")	#Give name of the website you wish to login



#signin = driver.find_element_by_link_text("#loginPage")
#signin.click()

### This is for special cases where application doesn't show the login fields directly
element = driver.find_element_by_partial_link_text('SIGN IN') #if the application possess a button to display the field for entering credentials
element.click() #this prompts the username and password fields
###


driver.implicitly_wait(10)   #implicit waiting

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.send_keys("user_name") #this sends the username
password.send_keys("password")	#this sends the password for corresponding username

driver.implicitly_wait(5)	#implicit waiting

form = driver.find_element_by_name('loginForm')

driver.implicitly_wait(5)	#implicit waiting

form.submit()
driver.quit()
