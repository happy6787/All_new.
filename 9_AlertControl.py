from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#btnclick=driver.find_element(By.CSS_SELECTOR,"#content > div > ul > li:nth-child(1) > button") #use css or xpath
#btnclick.click() ### for ok

#btnclick = driver.find_element(By.CSS_SELECTOR,"#content > div > ul > li:nth-child(2) > button") #use css or xpath
#btnclick.click() ### for dismiss



time.sleep(3)

#driver.switch_to.alert.accept() ###  click on ok
#driver.switch_to.alert.dismiss() ### click on cancle
#driver.switch_to.alert.send_keys()