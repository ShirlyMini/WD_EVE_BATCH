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

rt_clk=driver.find_element(By.XPATH, "//span[contains(text(),'right click me')]")
copy_option=driver.find_element(By.XPATH, "//span[contains(text(),'Copy')]")

act_obj.context_click(rt_clk).move_to_element(copy_option).click().perform()

alt = driver.switch_to.alert
print(alt.text)
alt.accept()

sleep(10)