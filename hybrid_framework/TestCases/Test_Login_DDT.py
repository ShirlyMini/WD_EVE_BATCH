import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import sys
sys.path.append("C:\\Users\\user\\PycharmProjects\\pythonProject_WE_MARCH")
print(sys.path)
from hybrid_framework.PageObject.nop_login import Login
from hybrid_framework.Utilities.ReadConfig import ReadProperty
from hybrid_framework.Utilities.CustomLogger import customlog
from hybrid_framework.TestData.LoadData import *

ss=r"C:\Users\user\PycharmProjects\pythonProject_WE_MARCH\hybrid_framework\ScreenShot"

class Test_Login_DDT_002:
    log=customlog()
    xpath=r"C:\Users\user\PycharmProjects\pythonProject_WE_MARCH\hybrid_framework\TestData\LoginData.xlsx"
    sheet="Sheet1"
    data=load_data_from_xl(xpath, sheet)

    @pytest.mark.parametrize("email, pswd, expected", data)
    def test_verify_dsahbord_page_title_ddt(self, launch_browser, email, pswd, expected):
        self.log.info("TC1::test_verify_dsahbord_page_title_ddt")
        driver = launch_browser
        login_obj=Login(driver)
        login_obj.SetEmail(email)
        login_obj.SetPassword(pswd)
        login_obj.ClickRemember()
        login_obj.ClickLogin()
        self.log.info("Logging into dashboard....")

        if driver.title == "Dashboard / nopCommerce administration" and expected=="Pass":
            self.log.info("TC1::test_verify_dsahbord_page_title_ddt=PASS")
            assert True
        elif driver.title != "Dashboard / nopCommerce administration" and expected=="Fail":
            self.log.info("TC1::test_verify_dsahbord_page_title=PASS")
            assert True
        else:
            self.log.error("TC1::test_verify_dsahbord_page_title_ddt=FAIL")
            driver.save_screenshot(ss+"\\"+"test_verify_dsahbord_page_title_ddt.png")
            assert False