# normal locator
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://admin-demo.nopcommerce.com/")
#####id
# email_we = driver.find_element(By.ID,"Email")
# email_we.clear()
# email_we.send_keys("admin@yourstore.com")
#
# password_we = driver.find_element(By.ID, "Password")
# password_we.clear()
# password_we.send_keys("admin")
#
# print(driver.find_element(By.ID,"Email"))
#
# driver.find_element(By.ID,"Email").clear()
# driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
# driver.find_element(By.ID, "Password").clear()
# driver.find_element(By.ID, "Password").send_keys("admin")

######name

# driver.find_element(By.NAME, "Email").clear()
# driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")
# driver.find_element(By.NAME, "Password").clear()
# driver.find_element(By.NAME, "Password").send_keys("admin")
#

#######Class

# driver.find_element(By.CLASS_NAME, "email").clear()
# driver.find_element(By.CLASS_NAME, "email").send_keys("admin@yourstore.com")
# driver.find_element(By.CLASS_NAME, "password").clear()
# driver.find_element(By.CLASS_NAME, "password").send_keys("admin")
#
# driver.find_element(By.CLASS_NAME, "button-1").click()
#
#
# sleep(10)

#####tagname

# print(driver.find_element(By.TAG_NAME, "h1").text)


####link text
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# sleep(3)
# driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

driver.get("https://www.orangehrm.com/")
sleep(3)
# driver.find_element(By.LINK_TEXT, "Accept Cookies").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Accept").click()

sleep(10)