import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com")
driver.maximize_window()

time.sleep(2)

driver.find_element(By.LINK_TEXT,"Multiple Windows").click()

time.sleep(3)

driver.find_element(By.LINK_TEXT,"Click Here").click()

time.sleep(2)

print(driver.window_handles)
driver.switch_to.window(driver.window_handles[-1]) ### -1 will always open last window
### from above(driver.window_handles) we get list of windows and from list we can use index to find or go to new window
#driver.switch_to.window(driver.window_handles[-1]) ### will get back to original window
#driver.window_handles("main")  ### will get back to original window >>> not working 

# driver.switch_to.window() ### will not work as we need new window name

newWindow = (driver.find_element(By.CSS_SELECTOR,"body > div > h3").get_attribute("innerHTML"))
print("text on new window is  : ", newWindow)
### will not work as we are not on the new window page but after switch to window it will work

print(driver.current_window_handle)

# driver.switch_to.window('main') ### will get back to original window
# print(driver.current_window_handle)