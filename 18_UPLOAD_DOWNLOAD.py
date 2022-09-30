import time

from selenium   import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")

driver.find_element(By.ID, "file-upload").send_keys("D:\OneDrive\Desktop\AK.jpg")
time.sleep(3)
driver.find_element(By.ID, "file-submit").click()

###################################################################################






