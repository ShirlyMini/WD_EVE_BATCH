# checkbox
#
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
sleep(2)
driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Catalog')]").click()
sleep(3)
driver.find_element(By.XPATH, "//ul[@role='menu']/li/ul/li/a/p[text()=' Products']").click()

#### to select single checkbox
# driver.find_element(By.XPATH, "//th/input[@class='mastercheckbox']").click()
# print(driver.find_element(By.XPATH, "//th/input[@class='mastercheckbox']").is_selected())#True

### to select mutiple checkbox

# list_of_elem = driver.find_elements(By.XPATH, "//input[@name='checkbox_products']")
#
# for elem in list_of_elem:
#     elem.click()
#     print(elem.is_selected())

# to select check box based on condition

we_row = driver.find_elements(By.XPATH, "//table[@id='products-grid']/tbody/tr")
# print(len(we_row))#15

# for r in range(len(we_row)):# row from 0 to 14
for r in range(1,len(we_row)+1):# row from 1 to 15
    price = driver.find_element(By.XPATH, f"//table[@id='products-grid']/tbody/tr[{r}]/td[5]").text
    if price != "":
        if float(price)>1000:
            driver.find_element(By.XPATH, f"//table[@id='products-grid']/tbody/tr[{r}]/td[1]/input").click()


sleep(10)