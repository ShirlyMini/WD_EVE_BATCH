from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://www.linkedin.com/learning-login/")
# driver.maximize_window()

# if driver.find_element(By.ID, "auth-id-input").is_displayed():
#     print(driver.find_element(By.ID, "auth-id-button").is_enabled())
#     # sleep(3)
#     driver.find_element(By.ID, "auth-id-input").send_keys("abc@gmail.com")
#     print(driver.find_element(By.ID, "auth-id-button").is_enabled())


###is selceted always works with input tag

# driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
# driver.maximize_window()
#
# print(driver.find_element(By.ID, "RememberMe").is_selected())# false
# driver.find_element(By.ID, "RememberMe").click()
# print(driver.find_element(By.ID, "RememberMe").is_selected())# true

####is selected without input tag
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
print(driver.find_element(By.XPATH, "//li[@data-cy='oneWayTrip']").is_selected())
print(driver.find_element(By.XPATH, "//li[@data-cy='roundTrip']").is_selected())
print(driver.find_element(By.XPATH, "//li[@data-cy='mulitiCityTrip']").is_selected())

