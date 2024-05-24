import datetime
import os
from time import sleep
import os
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.globalsqa.com/demo-site/datepicker/#Simple%20Date%20Picker")
driver.maximize_window()
driver.implicitly_wait(10)

dt=datetime.datetime(2024,10,28)
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']"))
driver.find_element(By.ID, "datepicker").click()
while True:
    year_dp = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    year = dt.strftime("%Y")
    if year_dp > year:
        driver.find_element(By.XPATH,"//span[text()='Prev']").click()
    elif year_dp < year:
        driver.find_element(By.XPATH, "//span[text()='Next']").click()
    else:
        break

month_dict = {"January": 1,
              "Febraury":2,
              "March":3,
              "April":4,
              "May":5,
              "June":6,
              "July":7,
              "August":8,
              "September":9,
              "October":10,
              "November":11,
              "December":12}

while True:
    month_dp = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    month = int(dt.strftime("%m").lstrip("0"))
    if month_dict[month_dp]>month:
        driver.find_element(By.XPATH, "//span[text()='Prev']").click()
    elif month_dict[month_dp]<month:
        driver.find_element(By.XPATH, "//span[text()='Next']").click()
    else:
        break

date=dt.strftime("%d").lstrip("0")
driver.find_element(By.XPATH,f"//tr/td/a[text()={date}]").click()

actual_date = driver.find_element(By.ID, "datepicker").get_attribute("value")
expected_date = dt.strftime("%m/%d/%Y")

assert actual_date==expected_date, "date picker not working properly"

sleep(10)