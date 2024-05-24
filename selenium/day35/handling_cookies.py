import os
from time import sleep
import os
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)

print(driver.get_cookies())

# [{'domain': 'admin-demo.nopcommerce.com', 'httpOnly': True, 'name': '.Nop.Antiforgery', 'path': '/', 'sameSite': 'Strict', 'secure': True, 'value': 'CfDJ8IiSoo1ocrtFvurdsk63e1RvwaOGotyrWj-WixyXlLgYsAPRPCfyQ_qijtBVDjnRXP9_-6ILuoem8FdEQYwIVJXHwNtrseopa1YMIhdULfGQvD4xVQ_P2WtUO4GZH65zL62qXe4-7R10Zv30_-BkLIA'},
#  {'domain': 'admin-demo.nopcommerce.com', 'expiry': 1746021390, 'httpOnly': False, 'name': '.Nop.Culture', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'c%3Den-US%7Cuic%3Den-US'},
#  {'domain': 'admin-demo.nopcommerce.com', 'expiry': 1746021390, 'httpOnly': True, 'name': '.Nop.Customer', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '4db9ff04-da7e-434a-8ce3-04174b1a0643'}]

### add cookie

driver.add_cookie({'name':'mycookie', 'value':"12345567jsxnsh"})
print(driver.get_cookies())

### delete cookie
driver.delete_cookie('mycookie')
print(driver.get_cookies())
driver.delete_all_cookies()
print(driver.get_cookies())