from data import *
from helpers import *
from test.locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:

    def test_registration_successful(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.SEARCH_INPUT_NAME).send_keys(registration_name)
        new_email = generate_new_email()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(new_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys(correct_password)
        driver.find_element(*TestLocators.CHECK_BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocators.SEARCH_BUTTON_LOGIN))
        check_text = driver.find_element(*TestLocators.SEARCH_BUTTON_LOGIN).text
        assert check_text == "Вход"

    def test_password_error(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.SEARCH_INPUT_NAME).send_keys(registration_name)
        new_email = generate_new_email()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(new_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys(incorrect_password)
        driver.find_element(*TestLocators.CHECK_BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ERROR_PASSWORD))
        check_text = driver.find_element(*TestLocators.SEARCH_ERROR_PASSWORD).text
        assert check_text == "Некорректный пароль"