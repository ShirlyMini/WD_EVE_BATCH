from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import sys
sys.path.append("C:\\Users\\user\\PycharmProjects\\pythonProject_WE_MARCH")
print(sys.path)
from hybrid_framework.PageObject.nop_login import Login
from hybrid_framework.PageObject.AddCustomers import AddCustomer
from hybrid_framework.Utilities.ReadConfig import ReadProperty
from hybrid_framework.Utilities.CustomLogger import customlog

ss=r"C:\Users\user\PycharmProjects\pythonProject_WE_MARCH\hybrid_framework\ScreenShot"

class Test_add_customer_003:
    log=customlog()
    def test_verify_add_customer(self, launch_browser):
        self.log.info("TC1::test_verify_add_customer")
        driver=launch_browser
        login_obj=Login(driver)
        login_obj.SetEmail(ReadProperty.GetUserName())
        login_obj.SetPassword(ReadProperty.GetPassword())
        login_obj.ClickRemember()
        login_obj.ClickLogin()
        self.log.info("Logging into dashboard....")
        ac_obj = AddCustomer(driver)
        ac_obj.NavigateCustomerPage()
        ac_obj.ClickAddNewCustomer()
        ac_obj.SetUsername("shirly123@gmail.com")
        ac_obj.SetPasword("123456")
        ac_obj.SetFirstname("pooja")
        ac_obj.SetLastname("venkat")
        ac_obj.selectGender("Female")
        ac_obj.SetDOB("02-10-1994")
        ac_obj.SetCompanyName("xyz company")
        ac_obj.ClickTaxExempt("yes")
        ac_obj.SelectNewsLetter("Test store 2")
        ac_obj.SelectCustomerRole("Administrators")
        ac_obj.SelectVendor("Vendor 1")
        ac_obj.ClickActive()
        ac_obj.SetAdminComment("this is admin")
        ac_obj.ClickSave()
        alt = ac_obj.VerifyAlert()
        print(alt)
        if "The new customer has been added successfully." in alt:
            self.log.info("TC1::test_verify_add_customer=PASS")
            assert True
        else:
            self.log.error("TC1::test_verify_add_customer=FAIL")
            driver.save_screenshot(ss+"\\"+"test_verify_add_customer_003.png")
            assert False

