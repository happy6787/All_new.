import pprint
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("file:///D:/SUCCESS/ACADEMICS/CREDENCE%20TESTING/SAGAR%20S/SELENIUM%20PRACTICALS/MultipleWindowsOpening/MultipleWindowsOpening.html")
driver.maximize_window()

parentGUID = driver.current_window_handle
print("parent id is : ", parentGUID)

driver.find_element(By.XPATH, "/html/body/div/a[1]").click()
driver.switch_to.window(driver.window_handles[1])
print((f"title is : {driver.title} & Id is : {driver.current_window_handle}"))
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/a[2]").click()
driver.switch_to.window(driver.window_handles[2])
print((f"title is : {driver.title} & Id is : {driver.current_window_handle}"))
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/a[3]").click()
driver.switch_to.window(driver.window_handles[3])
print((f"title is : {driver.title} & Id is : {driver.current_window_handle}"))
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/a[4]").click()
driver.switch_to.window(driver.window_handles[4])
print(f"title is : {driver.title} Id is : {driver.current_window_handle}")
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/a[5]").click()
driver.switch_to.window(driver.window_handles[5])
print(f"title is : {driver.title} & Id is : {driver.current_window_handle}")
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/a[6]").click()
driver.switch_to.window(driver.window_handles[6])
print(f"title is : {driver.title} & Id is : {driver.current_window_handle}")
driver.switch_to.window(driver.window_handles[0])
# time.sleep(3)

allGUID = driver.window_handles
print("all IDs : ", allGUID)

dicts = {}
keys = ['parent','fb','go','gm','az','fk','yt']
values =allGUID
for i in range(len(keys)):
    dicts[keys[i]] = values[i]
print(*dicts)

#################################################################################
# title = ['parent','yt','fk','az','gm','go','fb']
# handle = [allGUID]
# di = dict(zip(title,reversed(handle)))
# pprint.pprint(di)
################################################################################

# ## handles.find
# userinput = "Facebook.com"      ## input function
# all_handles = driver.window_handles
# for handle in all_handles:
#     driver.switch_to.window(handle)
#     print(driver.title)
#     print(driver.current_url)
#
#     if(driver.title == userinput):
#         break
## write logic to operate on facebook.com


## make entry to dictionary, key = titile/url , value = handle



















