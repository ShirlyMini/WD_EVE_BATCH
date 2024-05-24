#
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *


service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
wait_obj=WebDriverWait(driver, 300, poll_frequency=5, ignored_exceptions=[NoSuchElementException,
                                                                          ElementNotInteractableException])

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[@type='submit']").click()
wait_obj.until(expected_conditions.presence_of_element_located((By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Sales')]")))
driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Sales')]").click()

wait_obj.until(expected_conditions.visibility_of_element_located((By.XPATH, "//ul[@role='menu']/li/ul/li/a/p[contains(text(),'Shipments')]")))
driver.find_element(By.XPATH, "//ul[@role='menu']/li/ul/li/a/p[contains(text(),'Shipments')]").click()

print(driver.title)

sleep(10)