import os
from time import sleep
import os
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://books-pwakit.appspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

shadow_dom = driver.find_element(By.CSS_SELECTOR,'book-app').shadow_root

shadow_dom.find_element(By.ID, "input").send_keys("harry potter")

sleep(10)