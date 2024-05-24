import os
from time import sleep
import os
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
###download preference
location=os.getcwd()
print(location)

preference={"download.default_directory":location}
ch_op = webdriver.ChromeOptions()
ch_op.add_experimental_option("prefs", preference)
ch_op.add_argument("--headless")
ch_op.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(service=service_obj, options=ch_op)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
# driver.implicitly_wait(10)
wait = WebDriverWait(driver, 30)
####login
sleep(5)
driver.find_element(By.NAME, "Email").clear()
driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.NAME, "Password").clear()
driver.find_element(By.NAME, "Password").send_keys("admin")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
print(driver.title)
###using select menu
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Catalog')]")))
driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Catalog')]").click()
sleep(3)
driver.find_element(By.XPATH, "//ul[@role='menu']/li/ul/li/a/p[text()=' Products']").click()

####download file
driver.find_element(By.NAME, "download-catalog-pdf").click()
print(driver.title)
sleep(20)