from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()

driver.find_element(By.XPATH, "//img[@alt='fab_icon']").click()
# driver.close()### closes the driver focused page
driver.quit()

sleep(10)