import os
from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By


service_obj = Service(r"E:\selenium\drivers\msedgedriver.exe")
###download preference
location=os.getcwd()
print(location)

preference={"download.default_directory":location}
ch_op = webdriver.EdgeOptions()
ch_op.add_experimental_option("prefs", preference)

driver = webdriver.Edge(service=service_obj, options=ch_op)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)

####login
driver.find_element(By.XPATH, "//button[@type='submit']").click()

###using select menu
sleep(3)
driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Catalog')]").click()
sleep(3)
driver.find_element(By.XPATH, "//ul[@role='menu']/li/ul/li/a/p[text()=' Products']").click()

####download file
driver.find_element(By.NAME, "download-catalog-pdf").click()

sleep(20)