from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
driver.implicitly_wait(10)

# driver.find_element(By.XPATH,"//button[@class='btn btn-info']").click()
# print(driver.window_handles)#[parent, child1..., childn]#['F86B2406E949734C05D149D5EF055E5D', 'E2351EACF4F22107E457E869BA37C137']
# driver.switch_to.window(driver.window_handles[1])
# print(driver.title)

driver.find_element(By.XPATH, "//a[contains(text(),'Open New Seperate Windows')]").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
print(driver.window_handles)#['F0958FBB162BB32A5438863297BB49F5', 'E63274A635973BD53B9D0707F230FDAF']
driver.switch_to.window(driver.window_handles[1])
print(driver.title)