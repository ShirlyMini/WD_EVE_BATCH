# relative xpath
# //

#//tagname[@attr="attrvalue"]
#//*[@attr="attrvalue"]

#//input[@id="Email"]
#//input[@class="email valid"]
#//input[@name="Email"]


from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='Email']").clear()
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("admin@yourstore.com")
driver.find_element(By.XPATH,"//input[@type='password']").clear()
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("admin")
driver.find_element(By.XPATH,"//button[@class='button-1 login-button']").click()

sleep(10)

########################
# xpath option
# //input[@type='text' and @name='username']
#//input[@type='text' or @name='username']
# //input[contains(@type, 'xt')]
# //input[contains(@name, 'user')]
#//input[starts-with(@type, 'te')]
#//b[text()='Comments']

####//a[text()='Nagpur Power']--> doent match
# //a[contains(text(),'Nagpur Power')]
