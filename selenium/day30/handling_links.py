from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests


service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
driver.implicitly_wait(10)

links_we_list = driver.find_elements(By.XPATH, "//a")

for elem in links_we_list:
    try:
        url = elem.get_attribute("href")
        response = requests.get(url)
        # print(url, response.status_code)
        if response.status_code > 299:
            print(f"Broken Link:{url}::{response.status_code}")
        else:
            print(f"valid Link:{url}::{response.status_code}")
    except Exception as msg:
        print(f"Broken Link:{url}::{msg}")
