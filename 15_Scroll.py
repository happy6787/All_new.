import time
from selenium import webdriver


driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

time.sleep(3)
## page scroll by pixel


driver.execute_script("window.scrollBy(0,6000)")
### there is no function on selenium to execute scroll so we use java script
### 0 >>> horizontal scrolling   3000 >>> vertical scrolling (pixels)
### (x,y) x >>> positive value will scroll to the right & -x >>> negative value will scroll to the left (horizontal)
### (x,y) y >>> positive value will scroll to the bottom & -x >>> negative value will scroll to the top (vertical)
### window >>> default object created in java script
#
#
# time.sleep(3)
# ## page scroll by upto specific element
# ele = driver.find_element(By.ID,"Typing")
# driver.execute_script("arguments[0].scrollIntoView()",ele)
#
# time.sleep(3)
# ## page scroll by till end of page
# driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
### document is also an object


# time.sleep(3)
# ## page scroll by from end till upside using pixels
# driver.execute_script("window.scrollBy(0,-3000)")
#
# time.sleep(3)
## page scroll by from end to at top
#driver.execute_script("scrollTo(0,document.body.scrollTop)")
#driver.execute_script("window.scrollTo(0,0)")


### Also one more method:
#from selenium.webdriver.common.keys import Keys
#driver.find_element(By.TAG_NAME,"body").send_keys(Keys.CONTROL + Keys.HOME)






