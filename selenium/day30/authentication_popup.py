from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
#####################http://username:password@url
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
# driver.maximize_window()
#################autoit
import autoit

driver.get("https://the-internet.herokuapp.com/basic_auth")
driver.maximize_window()

autoit.win_wait_active("", 30)
autoit.send("admin{TAB}")
autoit.send("admin{TAB}")
autoit.send("{ENTER}")

sleep(10)

sleep(10)
