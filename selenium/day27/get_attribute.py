from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()

# print(driver.find_element(By.ID, "Email").text)
# print(driver.find_element(By.ID, "Password").text)
print(driver.find_element(By.ID, "Email").get_attribute("value"))
print(driver.find_element(By.ID, "Password").get_attribute("value"))
