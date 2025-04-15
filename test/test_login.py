from data import *
from test.locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    def test_log_in_main(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_LOGIN_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_BUTTON_LOGIN))
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(login_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys(login_password)
        driver.find_element(*TestLocators.CLICK_BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_BUTTON_ORDER))
        check_button = driver.find_element(*TestLocators.SEARCH_BUTTON_ORDER).text
        assert check_button == "Оформить заказ"

    def test_log_in_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_BUTTON_LOGIN))
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(login_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys(login_password)
        driver.find_element(*TestLocators.CLICK_BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_BUTTON_ORDER))
        check_button = driver.find_element(*TestLocators.SEARCH_BUTTON_ORDER).text
        assert check_button == "Оформить заказ"

    def test_log_in_registration_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.CHECK_BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_BUTTON_LOGIN))
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(login_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys(login_password)
        driver.find_element(*TestLocators.CLICK_BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_BUTTON_ORDER))
        check_button = driver.find_element(*TestLocators.SEARCH_BUTTON_ORDER).text
        assert check_button == "Оформить заказ"

    def test_log_in_password_recovery_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(*TestLocators.CHECK_BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_BUTTON_LOGIN))
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(login_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys(login_password)
        driver.find_element(*TestLocators.CLICK_BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_BUTTON_ORDER))
        check_button = driver.find_element(*TestLocators.SEARCH_BUTTON_ORDER).text
        assert check_button == "Оформить заказ"