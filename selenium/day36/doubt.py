import os
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
location=os.getcwd()
preference={"download.default_directory":location}
down = webdriver.ChromeOptions()
down.add_experimental_option("prefs", preference)
driver = webdriver.Chrome(service=service_obj, options=down)
down.add_experimental_option("prefs", preference)
driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element(By.XPATH, "//button[@type='submit']").click()
sleep(3)
driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Catalog')]").click()
sleep(3)
driver.find_element(By.XPATH, "//ul[@role='menu']/li/ul/li/a/p[text()=' Products']").click()
driver.find_element(By.NAME,"download-catalog-pdf").click()
sleep(20)