from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import sys
sys.path.append("C:\\Users\\user\\PycharmProjects\\pythonProject_WE_MARCH")
print(sys.path)
from hybrid_framework.PageObject.nop_login import Login
from hybrid_framework.Utilities.ReadConfig import ReadProperty
from hybrid_framework.Utilities.CustomLogger import customlog

ss=r"C:\Users\user\PycharmProjects\pythonProject_WE_MARCH\hybrid_framework\ScreenShot"

class Test_Login_001:
    log=customlog()
    def test_verify_launch_page_title(self, launch_browser):
        self.log.info("TC1::test_verify_launch_page_title")
        driver=launch_browser
        if driver.title=="Your store. Login":
            self.log.info("TC1::test_verify_launch_page_title=PASSED")
            assert True
        else:
            self.log.error("TC1::test_verify_launch_page_title=FAILED")
            driver.save_screenshot(ss+"\\"+"login_001.png")
            assert False

    def test_verify_dsahbord_page_title(self, launch_browser):
        self.log.info("TC2::test_verify_dsahbord_page_title")
        driver = launch_browser
        login_obj=Login(driver)
        login_obj.SetEmail(ReadProperty.GetUserName())
        login_obj.SetPassword(ReadProperty.GetPassword())
        login_obj.ClickRemember()
        login_obj.ClickLogin()
        self.log.info("Logging into dashboard....")
        if driver.title == "Dashboard / nopCommerce administration":
            self.log.info("TC2::test_verify_dsahbord_page_title=PASS")
            assert True
        else:
            self.log.error("TC2::test_verify_dsahbord_page_title=FAIL")
            driver.save_screenshot(ss+"\\"+"login_001.png")
            assert False