
from selenium   import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

actionobj = ActionChains(driver)

driver.implicitly_wait(5)

## drag and drop
drag1 = driver.find_element(By.ID,'box1')
drop1 = driver.find_element(By.ID,'box101')
actionobj.drag_and_drop(drag1,drop1).perform()

drag3 = driver.find_element(By.ID,'box3')
drop3 = driver.find_element(By.ID,'box103')
actionobj.drag_and_drop(drag3,drop3).perform()

drag2 = driver.find_element(By.ID,'box2')
drop2 = driver.find_element(By.ID,'box102')
actionobj.drag_and_drop(drag2,drop2).perform()

drag4 = driver.find_element(By.ID,'box4')
drop4 = driver.find_element(By.ID,'box104')
actionobj.drag_and_drop(drag4,drop4).perform()

drag5 = driver.find_element(By.ID,'box5')
drop5 = driver.find_element(By.ID,'box105')
actionobj.drag_and_drop(drag5,drop5).perform()

drag6 = driver.find_element(By.ID,'box6')
drop6 = driver.find_element(By.ID,'box106')
actionobj.drag_and_drop(drag6,drop6).perform()

drag7 = driver.find_element(By.ID,'box7')
drop7 = driver.find_element(By.ID,'box107')
actionobj.drag_and_drop(drag7,drop7).perform()