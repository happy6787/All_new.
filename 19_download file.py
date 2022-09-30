
from selenium   import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_experimental_option("prefs", {"download.default_directory" : "D:\\SUCCESS\\ACADEMICS\\CREDENCE TESTING\\SAGAR\\CT11 SELENIUM\\CT11_ALL NEW"})
driver = webdriver.Chrome(options=chromeoptions)
driver.get("https://the-internet.herokuapp.com/download")

driver.find_element(By.XPATH,"/html/body/div[2]/div/div/a[3]").click()

