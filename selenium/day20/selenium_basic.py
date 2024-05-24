from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver = webdriver.Chrome()# webpage

driver.get("https://www.selenium.dev/")
driver.maximize_window()
print(driver.title)
driver.get("https://www.facebook.com/")
print(driver.title)
driver.back()
print("After navigating back to selenium",driver.title)
driver.forward()
print("After navigating forward to facebook",driver.title)
driver.refresh()
print("After refresh- facebook",driver.title)
driver.minimize_window()
# driver.close()

