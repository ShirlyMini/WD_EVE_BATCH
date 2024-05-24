from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://ui.vision/demo/webtest/frames/")
driver.maximize_window()
driver.implicitly_wait(10)


fr1_we = driver.find_element(By.XPATH, "//html/frameset/frame[1]")
driver.switch_to.frame(fr1_we)#locator-xpath, id, name
driver.find_element(By.NAME, "mytext1").send_keys("frame1")

driver.switch_to.default_content()

fr2_we=driver.find_element(By.XPATH, "//frameset/frameset/frame[1]")
driver.switch_to.frame(fr2_we)
driver.find_element(By.NAME, "mytext2").send_keys("frame2")


## handson-frame3 and frame4

sleep(10)