from data import *
from test.locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogout:
    def test_log_out(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_LOGIN_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_BUTTON_LOGIN))
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(login_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys(login_password)
        driver.find_element(*TestLocators.CLICK_BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocators.SEARCH_BUTTON_PERSONAL_ACCOUNT))
        driver.find_element(*TestLocators.SEARCH_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocators.SEARCH_TEXT_PROFILE))
        driver.find_element(*TestLocators.SEARCH_BUTTON_LOGOUT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_BUTTON_LOGIN))
        check_button = driver.find_element(*TestLocators.SEARCH_BUTTON_LOGIN).text
        assert check_button == "Вход"