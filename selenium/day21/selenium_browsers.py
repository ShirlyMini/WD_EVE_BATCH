# X86 is a 32-bit architecture, while X64 is a 64-bit extension of X86.
# ctrl+shift+i
from selenium import webdriver
from selenium.webdriver.edge.service import Service
#
service_obj = Service(r"E:\selenium\drivers\msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)
from time import sleep

######firefox
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service

# driver = webdriver.Firefox()
# s_obj = Service(r"E:\selenium\drivers\geckodriver.exe")
# driver = webdriver.Firefox(service=s_obj)

driver.get("https://www.selenium.dev/")
driver.maximize_window()
# print(driver.title)
# driver.get("https://www.facebook.com/")
# print(driver.title)
# driver.back()
# print("After navigating back to selenium",driver.title)
# driver.forward()
# print("After navigating forward to facebook",driver.title)
# driver.refresh()
# print("After refresh- facebook",driver.title)
sleep(5)
driver.minimize_window()
sleep(25)
driver.close()



################


# <button --tag
# type="submit"--attr
# class="button-1 login-button" xpath="1">Log in</button>


# normal locator---id, class, name, tagname, link, partial link
# customised loc---css, xpath


# E:\selenium\drivers\edgedriver_win64\geckodriver.exe