from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/feedback")
driver.maximize_window()
driver.implicitly_wait(10)

act_obj = ActionChains(driver)
driver.find_element(By.NAME, "username").send_keys("abc@gmail.com")
# ctrl+a and ctr+c
act_obj.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
act_obj.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
# tab
act_obj.send_keys(Keys.TAB).perform()
# ctrl+v
act_obj.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
# tab
act_obj.send_keys(Keys.TAB).perform()
# ctrl+v
act_obj.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

sleep(10)