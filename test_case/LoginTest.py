import unittest
from selenium import webdriver
import HtmlTestRunner
import time

import sys
sys.path.append("E:/OnlyForPython/SELENIUM/Unit-Test-HTML-Reports-Page-Object-Model")
from pages.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    baseURL = "https://admin-demo.nopcommerce.com/"
    driver = webdriver.Chrome(
        executable_path="E:\OnlyForPython\SELENIUM\drivers\chromedriver_win32\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    def test_login(self):

        login_page = LoginPage(self.driver)
        login_page.setUserName('admin@yourstore.com')
        login_page.setPassword('admin')
        login_page.clickOnLogin()
        time.sleep(5)

        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, 'webpage title is not matched')

        login_page.clickOnLogout()

    @classmethod
    def tearDownClass(cls) -> None:
        # close the current instance of browser window
        cls.driver.close()
        # close the all open instance of browser window
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
