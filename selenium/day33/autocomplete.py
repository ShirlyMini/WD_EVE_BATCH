from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://jqueryui.com/autocomplete/#multiple")
driver.maximize_window()
driver.implicitly_wait(10)

driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))
driver.find_element(By.ID, "tags").send_keys("a")
sleep(3)
driver.find_element(By.ID, "tags").send_keys(Keys.ARROW_DOWN)
driver.find_element(By.ID, "tags").send_keys(Keys.ARROW_DOWN)
driver.find_element(By.ID, "tags").send_keys(Keys.ARROW_DOWN)
driver.find_element(By.ID, "tags").send_keys(Keys.ENTER)

sleep(10)

