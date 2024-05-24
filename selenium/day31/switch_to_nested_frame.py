from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://ui.vision/demo/webtest/frames/")
driver.maximize_window()
driver.implicitly_wait(10)

parent_fr_elem = driver.find_element(By.XPATH, "//frameset/frameset/frame[2]")
driver.switch_to.frame(parent_fr_elem)
driver.find_element(By.NAME,"mytext3").send_keys("frame3")

child_fr_elem = driver.find_element(By.XPATH, "//iframe")
driver.switch_to.frame(child_fr_elem)
driver.find_element(By.ID, 'i5').click()

driver.switch_to.parent_frame()
driver.find_element(By.NAME,"mytext3").clear()
driver.find_element(By.NAME,"mytext3").send_keys("after switch from child frame")

sleep(10)