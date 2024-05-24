from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
driver.implicitly_wait(10)

act_obj = ActionChains(driver)

l_sider = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[1]")
print(l_sider.location)#{'x': 59, 'y': 250}
act_obj.drag_and_drop_by_offset(l_sider,100, 0).perform()
print(l_sider.location)#{'x': 161, 'y': 250}

r_sider = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[2]")
print(r_sider.location)#{'x': 545, 'y': 250}
act_obj.drag_and_drop_by_offset(r_sider,-100,0).perform()
print(r_sider.location)#{'x': 443, 'y': 250}

###to take screen shot

driver.save_screenshot("drag_drop_offset.png")

sleep(10)

