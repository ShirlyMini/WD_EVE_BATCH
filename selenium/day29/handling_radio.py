from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.implicitly_wait(10)
input="roundTrip"
driver.find_element(By.XPATH, f"//li[@data-cy='{input}']").click()

sleep(10)