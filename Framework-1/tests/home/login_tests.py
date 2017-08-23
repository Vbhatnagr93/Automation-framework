from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import loginPage

class LoginTests():

    def test_validlogin(self):
        baseurl="https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseurl)

        lp = loginPage(driver)
        lp.login("test@email.com", "abcabc")

        userIcon = driver.find_element(By.XPATH, ".//*[@id='navbar']//span[text()='User Settings']" )
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login not successful")

ff = LoginTests()
ff.test_validlogin()


