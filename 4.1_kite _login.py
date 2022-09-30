import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("http://kite.zerodha.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

inputid=driver.find_element(By.ID,"userid")
inputid.send_keys("MG8014")

inputpass=driver.find_element(By.ID,"password")
inputpass.send_keys("")

time.sleep(2)
inputsubmit=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/div/div/form/div[4]/button")
inputsubmit.click()

time.sleep(5)
enterpin = driver.find_element(By.ID,"pin")
enterpin.send_keys("")

time.sleep(2)
continuebtn = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/div/div/form/div[3]/button")
continuebtn.click()

time.sleep(2)

logout=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[2]/div/a/span").click()

time.sleep(2)

#logout1=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[2]/div/div/ul/li[10]/a").click()




