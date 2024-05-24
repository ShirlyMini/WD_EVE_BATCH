from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
sleep(2)
###using select and opition tags
# driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Catalog')]").click()
# sleep(3)
# driver.find_element(By.XPATH, "//ul[@role='menu']/li/ul/li/a/p[text()=' Products']").click()
#
# sleep(3)



# drp_dwn_elem = driver.find_element(By.NAME, 'products-grid_length')
#
# drp_down_obj = Select(drp_dwn_elem)
# # appr1
# drp_down_obj.select_by_visible_text("20")
# sleep(3)
# print(driver.find_element(By.ID, "products-grid_info").text)
# # appr2
# drp_down_obj.select_by_value("7")
# sleep(3)
# print(driver.find_element(By.ID, "products-grid_info").text)
# # appr3
# drp_down_obj.select_by_index(3)# 0 to n-1
# sleep(3)
# print(driver.find_element(By.ID, "products-grid_info").text)
# sleep(10)

###without select option


driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'System')]").click()
sleep(3)
option_xpath="//ul[@role='menu']/li/a/p[contains(text(),'System')]/parent::a/following-sibling::ul/li/a/p"
list_of_elem = driver.find_elements(By.XPATH, option_xpath)

for elem in list_of_elem:
    print(elem.text)