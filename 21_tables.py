
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/html/html_tables.asp")

# #print company
# print(driver.find_element(By.XPATH,"/html/body/div[7]/div[1]/div[1]/div[3]/div/table/tbody/tr[1]/th[1]").get_attribute('innerHTML'))
# print(driver.find_element(By.XPATH,"//*[@id='customers']/tbody/tr[1]/th[1]").text)
# 
# #print contact
# print(driver.find_element(By.XPATH,"//*[@id='customers']/tbody/tr[1]/th[2]").text)

#### print count of rows and columns using length function

rows = len(driver.find_elements(By.XPATH,"//*[@id='customers']/tbody/tr"))

columns = len(driver.find_elements(By.XPATH,"//*[@id='customers']/tbody/tr[1]/th"))

print(rows)
print(columns)

#### print count of rows and columns using __len__()
# print(driver.find_elements(By.XPATH,"//*[@id='customers']/tbody/tr").__len__())
#
# print(driver.find_elements(By.XPATH,"//*[@id='customers']/tbody/tr[1]/th").__len__())

#####################################################################################################3

### print all table values by  using loop

# table =  driver.find_element(By.ID,"customers")
# headers = driver.find_elements(By.TAG_NAME,"th")
# body = table.find_element(By.TAG_NAME,"tbody")
# cells = body.find_elements(By.TAG_NAME,"td")
#
# for  headerEle in headers:
#     print((headerEle.text))
#
# for cell in cells:
#     print(cell.text)

##################################################################################

#
# iValue = driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr')
#
# for i in range(1, len(iValue)):
#     print(iValue[i].text)

##################################################################################

AllEle = driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr')

for elements in AllEle:
    print(elements.text)

##################################################################################

# for r in range(2, rows + 1):
#     for p in range(1, columns + 1):
#         value = driver.find_element(By.XPATH,("//*[@id='customers']/tbody/tr[" + str(r) + "]/td[" + str(p) + "]")).text
#         print(value, end='       ')
#     print()
