from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/gainers")
driver.maximize_window()

###find element with single matching locator

# var=driver.find_element(By.XPATH,"//a[contains(text(), 'Senco Gold')]")
# print(var.text)
# var.click()
# print(driver.title)

###find elements with single matching locator
# list_of_elem=driver.find_elements(By.XPATH,"//a[contains(text(), 'Senco Gold')]")
# print(list_of_elem)
# for elem in list_of_elem:
#     print(elem.text)

### find elemnts with multiple matching locator

# list_of_elem=driver.find_elements(By.XPATH,"//a[contains(text(), 'Gold')]")
# print(list_of_elem)
# for elem in list_of_elem:
#     print("text", elem.text)
#     # elem.click()
    # print("title", driver.title)
    # driver.back()
    # sleep(5)

# find elemnts with single matching locator - return first matching elem

# print(driver.find_element(By.XPATH,"//a[contains(text(), 'Gold')]").text)

### with invalid locator

# print(driver.find_element(By.XPATH,"//a[contains(text(), 'xwxewdcweqdf')]"))#NoSuchElementException
print(driver.find_elements(By.XPATH,"//a[contains(text(), 'xwxewdcweqdf')]"))#[]