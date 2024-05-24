import datetime
import os
from time import sleep
import os
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.globalsqa.com/demo-site/datepicker/#Simple%20Date%20Picker")
driver.maximize_window()
driver.implicitly_wait(10)
dt = datetime.datetime.now().strftime("%m/%d/%Y")
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']"))
driver.find_element(By.ID,"datepicker").send_keys(dt)

sleep(10)