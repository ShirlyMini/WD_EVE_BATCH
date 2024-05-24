from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()

#### css---> tagname is optional
###tagname#valueofid or
# #valueofid
# tagname.valueofclass
# .valueofclass
#tagname[attrname=attrvalue]
# [attrname=attrvalue]

# tagname#idvalue.valueofclass[attrname=attrvalue]
# #idvalue.valueofclass[attrname=attrvalue]


# driver.find_element(By.CSS_SELECTOR, "input#Email").clear()
# driver.find_element(By.CSS_SELECTOR, "input#Email").send_keys("admin@yourstore.com")
# driver.find_element(By.CSS_SELECTOR, "input#Password.password").clear()
# driver.find_element(By.CSS_SELECTOR, "input#Password.password").send_keys("admin")
# driver.find_element(By.CSS_SELECTOR, "button.button-1.login-button").click()
####without tagname
# driver.find_element(By.CSS_SELECTOR, "#Email").clear()
# driver.find_element(By.CSS_SELECTOR, "#Email").send_keys("admin@yourstore.com")
# driver.find_element(By.CSS_SELECTOR, "#Password.password").clear()
# driver.find_element(By.CSS_SELECTOR, "#Password.password").send_keys("admin")
# driver.find_element(By.CSS_SELECTOR, ".button-1.login-button").click()


#####with id or classvalue
# driver.find_element(By.CSS_SELECTOR, "input[name=Email]").clear()
# driver.find_element(By.CSS_SELECTOR, "input[name=Email]").send_keys("admin@yourstore.com")
# driver.find_element(By.CSS_SELECTOR, "input[name=Password]").clear()
# driver.find_element(By.CSS_SELECTOR, "input[name=Password]").send_keys("admin")
# driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

# driver.find_element(By.CSS_SELECTOR, "[name=Email]").clear()
driver.find_element(By.CSS_SELECTOR, "[id=Email]").clear()
driver.find_element(By.CSS_SELECTOR, "[name=Email]").send_keys("admin@yourstore.com")
driver.find_element(By.CSS_SELECTOR, "[name=Password]").clear()
driver.find_element(By.CSS_SELECTOR, "[name=Password]").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, "[type=submit].button-1").click()


sleep(10)