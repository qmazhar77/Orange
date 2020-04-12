from PytestDemo.OrangeHRMProject.Locators.Locators import locators

class loginPage:
    def __init__(self,driver):
        self.driver = driver

        self.username_text_id = locators.txtusername_id
        self.password_text_id = locators.txtpassword_id
        self.login_btn = locators.btnlogin_id

    def enter_username(self,username):

        self.driver.find_element_by_id(self.username_text_id).clear()
        self.driver.find_element_by_id(self.username_text_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_text_id).clear()
        self.driver.find_element_by_id(self.password_text_id).send_keys(password)

    def click_loginbtn(self):
        self.driver.find_element_by_id(self.login_btn).click()