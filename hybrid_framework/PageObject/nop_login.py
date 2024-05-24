from selenium.webdriver.common.by import By


class Login:
    id_email="Email"
    id_password="Password"
    id_rememberme="RememberMe"
    xpath_login="//button[@type='submit']"

    def __init__(self, driver):
        self.driver=driver

    def SetEmail(self,email):
        self.driver.find_element(By.ID, self.id_email).clear()
        self.driver.find_element(By.ID, self.id_email).send_keys(email)

    def SetPassword(self, pswd):
        self.driver.find_element(By.ID, self.id_password).clear()
        self.driver.find_element(By.ID, self.id_password).send_keys(pswd)

    def ClickRemember(self):
        self.driver.find_element(By.ID, self.id_rememberme).click()

    def ClickLogin(self):
        self.driver.find_element(By.XPATH, self.xpath_login).click()
