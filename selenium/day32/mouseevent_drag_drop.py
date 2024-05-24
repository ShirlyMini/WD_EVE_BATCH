from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
driver.implicitly_wait(10)

act_obj = ActionChains(driver)

s1=driver.find_element(By.ID, "box1")
d1=driver.find_element(By.ID, "box101")
s2=driver.find_element(By.ID, "box2")
d2=driver.find_element(By.ID, "box102")
s3=driver.find_element(By.ID, "box3")
d3=driver.find_element(By.ID, "box103")

act_obj.drag_and_drop(s1,d1).drag_and_drop(s2,d2).drag_and_drop(s3,d3).perform()

sleep(10)