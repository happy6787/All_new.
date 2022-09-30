from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")

inputstr=driver.find_element(By.ID,"myTextInput2")
# c
# #print("input text :", inputstr)
# print("input text :",inputstr.get_attribute("type"))
# print("input id :",inputstr.get_attribute("id"))
# print("input value :",inputstr.get_attribute("value"))
# print("input name :",inputstr.get_attribute("name"))
print("input text :",inputstr.clear())
inputstr.send_keys("happy")