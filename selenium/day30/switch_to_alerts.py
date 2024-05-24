from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.implicitly_wait(10)

# alert_general
# driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
# alt_ref = driver.switch_to.alert
# print(alt_ref.text)
# alt_ref.accept()
# print(driver.find_element(By.ID, "result").text)
# sleep(10)

# confirm_alert
# driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
# alt_ref = driver.switch_to.alert
# sleep(5)
# print(alt_ref.text)
# # alt_ref.accept()# click ok
# alt_ref.dismiss()# click cancel
# print(driver.find_element(By.ID, "result").text)
# sleep(10)

# prompt_alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
alt_ref = driver.switch_to.alert
sleep(3)
print(alt_ref.text)
alt_ref.send_keys("welcome")
alt_ref.accept()
print(driver.find_element(By.ID, "result").text)
sleep(10)