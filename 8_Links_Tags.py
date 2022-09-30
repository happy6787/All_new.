
### jo b links/urls honge usko tags, anchor tags (a) kahenge

##<a id="myLink1" name="linkName1" class="linkClass" href="https://seleniumbase.com">seleniumbase.com</a>
                                                                                    ### inner text / inner html
### if href is changed the link/url or page will change
### if inner html is changed, url name on page will change but link will be "href" only

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
driver.maximize_window()

### task to print all links visible text and href on web page
time.sleep(3)

links = driver.find_elements(By.TAG_NAME, "a")


for i in links:
    print(f'text is : , {i.text} \n link is : {i.get_attribute("href")}')




