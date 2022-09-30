
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.lambdatest.com/blog/python-selenium-screenshots/")


###relative path : with respect to current working directory.. where your executing script is located

### in same directory it will save the image (we cans ee in left side)
#driver.get_screenshot_as_file("facebookLoginTest.png")


### will save in same directory but in specified folder (here scrnshot)
#driver.get_screenshot_as_file("scrnshot\\20.3_facebookLoginTest.png")


### will save in same directory but in last second folder because we have given (..\\)
#driver.get_screenshot_as_file("..\\20.3_facebookLoginTest.png")  ### 1 parent up folder
#driver.get_screenshot_as_file("..\\..\\FacebookLoginTest.png")   ### 2 parent up folder

###############################################################################################

##Absoult path (full path) :
#driver.get_screenshot_as_file("D:\\OneDrive\\Desktop\\FacebookLoginTest.png")


### another method
driver.save_screenshot("FacebookLoginTestwithoutext")
### above we acn use both absolute and relative path

### jab kisi specific path pe save karna hai uske liye absolute method/path use kare
### jab same directory me save karna hai to uske liye relative path use kare


