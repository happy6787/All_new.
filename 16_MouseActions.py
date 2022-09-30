import time

from selenium   import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")

# driver.find_element(By.ID, 'myDropdown').click()
# driver.find_element(By.ID, 'dropOption2').click()
#### element not interactable # we can not directly reach to element before reaching to parent

hoverele = driver.find_element(By.ID, 'myDropdown')
optionele = driver.find_element(By.ID, 'dropOption2')

actionobj = ActionChains(driver)
actionobj.move_to_element(hoverele).move_to_element(optionele).click().perform()

####################################################################################################

## double click

btn = driver.find_element(By.ID,"myButton")
actionobj.double_click(btn).perform()
time.sleep(3)
driver.find_element(By.ID,"myButton").click()
time.sleep(2)
driver.find_element(By.ID,"myButton").click()
actionobj.double_click(btn).perform()

####################################################################################################

## right click

actionobj.context_click().perform()
### will perform where the last location of cursor was

time.sleep(3)

contextclck = driver.find_element(By.ID,"myTextInput2")
actionobj.context_click(contextclck).perform()

####################################################################################################

## drag and drop
driver.find_element(By.ID,"checkBox1").click()
drag = driver.find_element(By.XPATH,'//*[@id="logo"]')
drop = driver.find_element(By.ID,'drop2')
actionobj.drag_and_drop(drag,drop).perform()


