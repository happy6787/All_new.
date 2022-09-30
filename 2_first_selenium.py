
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('http://facebook.com')
# driver.maximize_window()

#####################################################################################

# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path=r"D:\SUCCESS\ACADEMICS\CREDENCE TESTING\SAGAR S\chromedriver_win32\chromedriver.exe")
# driver.get('http://facebook.com'), driver.maximize_window()

#####################################################################################
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service(r"D:\SUCCESS\ACADEMICS\CREDENCE TESTING\SAGAR S\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('http://facebook.com'), driver.maximize_window()
print("Page Title: ",driver.title)
print("Page Current url: ",driver.current_url)

driver.get('http://amazon.com'), driver.maximize_window()
print("Page Title: ",driver.title)
print("Page Current url: ",driver.current_url)

driver.back()

time.sleep(5)                     ###delays execution for given number of seconds
#time.sleep(2*60)               ### will delay for 2 mins
driver.forward()
#################################################

# driver1 = webdriver.Chrome(service=s)                    ####for new window assign new dri ver
# driver1.get('http://flipkart.com'), driver1.maximize_window()
# print("Page Title: ",driver1.title)
# print("Page Current url: ",driver1.current_url)
#

# driver.close()      ## will close only curent browser window
# driver.quit()       ##will close all the windows opened by script and also closes driver

### if you have method which doesn't require any arguments, and return some type of value amke it as property
### by using @ property decorator
### when you are calling it no need to give bracket like method call and use like

# LOCATORS
# ID - value will be unique on page
# NAME -  Value can be duplicate