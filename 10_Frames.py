import time

time.sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")

time.sleep(3)

driver.switch_to.frame("iframeResult")
driver.find_element(By.XPATH,"/html/body/button").click()
time.sleep(5)

driver.switch_to.alert.accept()