from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
driver.implicitly_wait(10)

act_obj=ActionChains(driver)

course1=driver.find_element(By.XPATH, "//span[text()='Courses']")
course2=driver.find_element(By.XPATH, "//span[text()='For Working Professionals']")
course3=driver.find_element(By.XPATH, "//a[text()='DevOps Engineering (LIVE)']")
act_obj.move_to_element(course1).move_to_element(course2).move_to_element(course3).click().perform()

print(driver.title)

sleep(10)