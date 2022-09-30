# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://amazon.com")
#
# print(driver.title)
# print(driver.current_url)
#
#
# inputsignin = driver.find_element(By.CLASS_NAME,"nav-line-1-container").click()  ### to find web control whose name is email
#
# inputemail = driver.find_element(By.NAME,"email")
# inputemail.send_keys("cabhinav724@gmail.com")
# btnsubmit = driver.find_element(By.ID,"continue")
# btnsubmit.click()
#
# inputpass = driver.find_element(By.NAME,"password")
# inputpass.send_keys("Abhi@1995")
#
# btnsignin = driver.find_element(By.ID,"signInSubmit")
# btnsignin.click()
# time.sleep(5)
#
# searchbox = driver.find_element(By.ID,"twotabsearchtextbox")
# searchbox.send_keys("apple iphone 12 mini")
# clicksearchbutton = driver.find_element(By.ID,"nav-search-submit-button").click()
#
# resultclick = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span").click()
# buynow = driver.find_element(By.ID,"buy-now-button").click()
# time.sleep(5)
#
# driver.back()
# time.sleep(3)
#
# driver.forward()
# time.sleep(5)
#
# driver.close()
# driver.quit()
#
