import os
from time import sleep
import os
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/gainers")
driver.maximize_window()
driver.implicitly_wait(10)

###row(tr) and col(td)

# print(driver.find_element(By.XPATH, "//table[@class='dataTable']/tbody/tr[4]/td[1]").text)
# print(driver.find_element(By.XPATH, "//table[@class='dataTable']/tbody/tr[5]/td[1]").text)
# print(driver.find_element(By.XPATH, "//table[@class='dataTable']/tbody/tr[6]/td[1]").text)

### collect data from specific row

# row_elem = driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr[4]/td")
# for i in row_elem:
#     print(i.text)

### collect data from specific col

# col_elem = driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr/td[1]")
# for i in col_elem:
#     print(i.text)

#### webscrapping


row = len(driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr"))# collects all rows# 1805
col = len(driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr[1]/td"))# collects all col # 5


for r in range(1,row+1):#1-1805# 0 to 1804
    for c in range(1,col+1):#1-5 # 0 to 4
        print(driver.find_element(By.XPATH, f"//table[@class='dataTable']/tbody/tr[{r}]/td[{c}]").text,end="\t")
    print("\n")
