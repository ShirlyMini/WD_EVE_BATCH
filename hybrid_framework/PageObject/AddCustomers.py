from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    xpath_customer_menu = "//ul[@role ='menu']/li/a/p[contains(text(),'Customers')]"
    xpath_customer_option = "//ul[@role='menu']/li/ul/li/a/p[text()=' Customers']"
    xpath_add_new_button = "//a[@class='btn btn-primary']"
    id_email_input = "Email"
    id_pswd_input = "Password"
    id_fname_input = "FirstName"
    id_lname_input = "LastName"
    id_gender_male = "Gender_Male"
    id_gender_female = "Gender_Female"
    id_dob_input = "DateOfBirth"
    id_company_input = "Company"
    id_taxexempt_checkbox = "IsTaxExempt"
    id_newsletter_select = "SelectedNewsletterSubscriptionStoreIds"
    id_customerrole_select = "SelectedCustomerRoleIds"
    id_vendor_select = "VendorId"
    id_active_checkbox = "Active"
    id_admin_input = "AdminComment"
    xpath_save = "//button[@name='save']"
    xpath_page_alert = "//div[@class='alert alert-success alert-dismissable']"

    def __init__(self, driver):
        self.driver=driver

    def NavigateCustomerPage(self):
        sleep(3)
        self.driver.find_element(By.XPATH, self.xpath_customer_menu).click()
        sleep(3)
        self.driver.find_element(By.XPATH, self.xpath_customer_option).click()

    def ClickAddNewCustomer(self):
        self.driver.find_element(By.XPATH, self.xpath_add_new_button).click()

    def SetUsername(self, email):
        self.driver.find_element(By.ID, self.id_email_input).send_keys(email)

    def SetPasword(self, pswd):
        self.driver.find_element(By.ID, self.id_pswd_input).send_keys(pswd)

    def SetFirstname(self, name):
        self.driver.find_element(By.ID, self.id_fname_input).send_keys(name)

    def SetLastname(self, name):
        self.driver.find_element(By.ID, self.id_lname_input).send_keys(name)

    def selectGender(self, gender):
        if gender.lower() == "male":
            self.driver.find_element(By.ID, self.id_gender_male).click()
        elif gender.lower() == "female":
            self.driver.find_element(By.ID, self.id_gender_female).click()
        else:
            raise Exception(f"{gender} option is not available")

    def SetDOB(self, date):
        self.driver.find_element(By.ID, self.id_dob_input).send_keys(date)

    def SetCompanyName(self, company):
        self.driver.find_element(By.ID, self.id_company_input).send_keys(company)

    def ClickTaxExempt(self, exempt):
        if exempt == "yes":
            self.driver.find_element(By.ID, self.id_taxexempt_checkbox).click()

    def SelectNewsLetter(self, letter):
        drp_down = Select(self.driver.find_element(By.ID, self.id_newsletter_select))
        drp_down.select_by_visible_text(letter)

    def SelectCustomerRole(self, role):
        drp_down = Select(self.driver.find_element(By.ID, self.id_customerrole_select))
        if role != "Registered":
            drp_down.select_by_visible_text(role)


    def SelectVendor(self, vendor):
        drp_down = Select(self.driver.find_element(By.ID, self.id_vendor_select))
        drp_down.select_by_visible_text(vendor)

    def ClickActive(self):
        self.driver.find_element(By.ID, self.id_active_checkbox).click()

    def SetAdminComment(self, msg):
        self.driver.find_element(By.ID, self.id_admin_input).send_keys(msg)

    def ClickSave(self):
        self.driver.find_element(By.XPATH, self.xpath_save).click()

    def VerifyAlert(self):
        return self.driver.find_element(By.XPATH, self.xpath_page_alert).text