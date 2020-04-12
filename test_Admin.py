from selenium import webdriver
import unittest
from PytestDemo.OrangeHRMProject.PageLayer.test_OrangeLoginPage import loginPage
from PytestDemo.OrangeHRMProject.PageLayer.test_UserManagmentPage import userPage
import sys
import os
from PytestDemo.OrangeHRMProject.Locators.Locators import locators
sys.path.append(os.path.join(os.path.dirname(__file__),"...","..."))

class test_valid_login(unittest.TestCase):

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()

        login = loginPage(self.driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_loginbtn()

        userp = userPage(self.driver)
        userp.clcik_user()
        userp.enter_search_user_name("robert.craig")
        userp.select_user_rol("ESS")
        userp.enter_emp_name("Robert Craig")
        userp.select_status("Enabled")
        userp.click_serach_btn()
        self.driver.implicitly_wait(20)
        self.driver.save_screenshot("D://Azhar Python/PythonFramework/serach.png")
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

# C:\Users\junaid\PycharmProjects\Demo> python -m PytestDemo.OrangeHRMProject.TestLayer.test_OrangeLogin

#below command use when we used pytest module
# venv) C:\Users\junaid\PycharmProjects\Demo\PytestDemo\OrangeHRMProject\TestLayer>pytest -v -s C:\Users\junaid\PycharmProjects\Demo\PytestDemo\OrangeHRMProject\TestLayer\
