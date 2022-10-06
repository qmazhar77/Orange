from PytestDemo.OrangeHRMProject.Locators.Locators import locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
class userPage:
    def __init__(self, driver):
        self.driver = driver

        self.adminmodule_id = locators.lnkadmin_id
        self.usermodule_id = locators.lnkusermgn_id
        self.userlink_id = locators.lnkuser_id

        
        self.user_search_text_id = locators.txtuserserach_id
        self.drp_user_rol_id = locators.drpuserrol_id
        self.emp_name_text_id = locators.txtempname_id
        self.drp_status_id = locators.drpstatus_id
        self.btn_search_id = locators.btnserach_id
        self.btn_reset_id = locators.btnreset_id

    def clcik_user(self):
        admin = self.driver.find_element_by_id(self.adminmodule_id)
        userm = self.driver.find_element_by_id(self.usermodule_id)
        user = self.driver.find_element_by_id(self.userlink_id)

        actions = ActionChains(self.driver)
        actions.move_to_element(admin).move_to_element(userm).move_to_element(user).click().perform()

    def enter_search_user_name(self,search_username):
        self.driver.find_element_by_id(self.user_search_text_id).send_keys(search_username)

    def select_user_rol(self,user):
        user_rol_element = self.driver.find_element_by_id(self.drp_user_rol_id)
        user_rol_drp = Select(user_rol_element)
        user_rol_drp.select_by_visible_text(user)

    def enter_emp_name(self,empname):
        self.driver.find_element_by_id(self.emp_name_text_id).send_keys(empname)

    def select_status(self,status):
        status_elemnt = self.driver.find_element_by_id(self.drp_status_id)
        status_drp = Select(status_elemnt)
        status_drp.select_by_visible_text(status)

    def click_serach_btn(self):
        self.driver.find_element_by_id(self.btn_search_id).click()

    def click_reset_btn(self):
        self.driver.find_element_by_id(self.btn_reset_id).click()


