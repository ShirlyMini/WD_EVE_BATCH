import os
from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By


# service_obj = Service(r"E:\selenium\drivers\msedgedriver.exe")
###download preference
location=os.getcwd()

ff_op = webdriver.FirefoxOptions()
ff_op.set_preference("browser.download.folderList",2)##0-desktop,1on-downloadfolder,2-desiredloc
ff_op.set_preference("browser.download.dir",location)#onlythefolderlistis2
driver = webdriver.Firefox(options=ff_op)

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
sleep(3)
####download file
driver.find_element(By.NAME, "download-catalog-pdf").click()

sleep(20)