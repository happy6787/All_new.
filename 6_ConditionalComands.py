from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")

#####################

#isdisplayed

#inputelement1=driver.find_element(By.ID,"myTextInput2")
#print("is drop option displayed :",inputelement1.is_displayed())

#print("is drop option displayed :",driver.find_element(By.ID,"myTextInput2").is_displayed())

################################################################################################

#isselected

#inputelement2=driver.find_element(By.ID,"radioButton2").click()

#print("is radio btn selected :",driver.find_element(By.ID,"radioButton1").is_selected())

# if driver.find_element(By.ID,"radioButton1").is_selected() == 1:
#     print("Pass")
# else:
#     print("Fail")

#################################################################################################

# print("is logo displayed :", driver.find_element(By.ID, "logo").is_displayed())
# if driver.find_element(By.ID,"logo").is_displayed() == 1:
#     print("visible")
# else:
#     print("not visible")
#
# inputelement3=driver.find_element(By.ID,"checkBox1").click()
#
# print("is logo displayed :",driver.find_element(By.ID,"logo").is_displayed())
# if driver.find_element(By.ID,"logo").is_displayed() == 1:
#     print("visible")
# else:
#     print("not visible")

############################################################################################

#isenabled

inputelement1=driver.find_element(By.ID,"myTextInput2")
print("is box enabled :",inputelement1.is_enabled())

print("is box enabled :",inputelement1.get_attribute("readonly"))
print("is box enabled :",inputelement1.get_attribute("disabled"))