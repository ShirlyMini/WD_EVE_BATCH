from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
driver.implicitly_wait(10)
## to scroll by amount
# driver.execute_script("window.scrollTo(0,1000)")
# sleep(3)
# print(driver.execute_script("return window.pageXOffset;"))
# print(driver.execute_script("return window.pageYOffset;"))

# scroll to elem

# web_elem = driver.find_element(By.XPATH, "//div[contains(text(),'Data Science with Python')]")
# driver.execute_script("arguments[0].scrollIntoView();", web_elem)
# sleep(3)
# print(driver.execute_script("return window.pageXOffset;"))
# print(driver.execute_script("return window.pageYOffset;"))


# scroll to bottom
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(3)
print(driver.execute_script("return window.pageXOffset;"))
print(driver.execute_script("return window.pageYOffset;"))

# scroll to top
driver.execute_script("window.scrollTo(0,0)")
sleep(3)
print(driver.execute_script("return window.pageXOffset;"))
print(driver.execute_script("return window.pageYOffset;"))
sleep(10)