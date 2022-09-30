import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
driver.maximize_window()

time.sleep(3)
# manual way to click >>> not to be used
# dropoption=driver.find_element(By.XPATH, "//*[@id='mySelect']/option[3]").click()

################################################################

time.sleep(3)

dropoption = driver.find_element(By.ID, "mySelect")
dropdownobj = Select(dropoption)
# dropdownobj.select_by_visible_text("Set to 50%")


# time.sleep(3)
#
# dropdownobj.select_by_visible_text("Set to 25%")

# time.sleep(3)
#
# dropdownobj.select_by_value("25%")
#
# time.sleep(3)
#
# dropdownobj.select_by_index(2)

####################################################################################

# #options
#
# happy = dropdownobj.options
# print("count of options :",len(happy))

####################################################################################
### task to print all options
alloptions = dropdownobj.options
#by text
for i in alloptions:
    #print("text is : ", i.text)

# by index

    #print("index is :", i.get_attribute('index'))

#by value:

    #print("value is: ", i.get_attribute("value"))
    print(f'text is : {i.text} \n value is : {i.get_attribute("value")} \n index is : {i.get_attribute("index")} ')



