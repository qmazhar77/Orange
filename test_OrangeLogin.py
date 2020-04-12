from selenium import webdriver
import unittest
from PytestDemo.OrangeHRMProject.PageLayer.test_OrangeLoginPage import loginPage
import sys
import os
from PytestDemo.OrangeHRMProject.Locators.Locators import locators
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))

class test_valid_login(unittest.TestCase):

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()

        login = loginPage(self.driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_loginbtn()

        self.driver.close()


if __name__ == '__main__':
    unittest.main()

# C:\Users\junaid\PycharmProjects\Demo> python -m PytestDemo.OrangeHRMProject.TestLayer.test_OrangeLogin
