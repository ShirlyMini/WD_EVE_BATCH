from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
driver.implicitly_wait(10)

act_obj = ActionChains(driver)

double_clk = driver.find_element(By.XPATH, "//button[contains(text(),'Double-Click Me To See Alert')]")

act_obj.double_click(double_clk).perform()

alt = driver.switch_to.alert
print(alt.text)
alt.accept()

sleep(10)