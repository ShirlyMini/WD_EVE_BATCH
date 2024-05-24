from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

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

####upload file
driver.find_element(By.NAME, "importexcel").click()
sleep(2)
file_path= r"/selenium/day34/orders.xlsx"
driver.find_element(By.ID,"importexcelfile").send_keys(file_path)

sleep(10)