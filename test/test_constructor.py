from test.locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSectionConstructor:
    def test_check_operation_fillings(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_FILLINGS).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocators.CHECK_SECTION_FILLINGS))
        check_text = driver.find_element(*TestLocators.CHECK_SECTION_FILLINGS).text
        assert check_text == "Начинки"

    def test_check_operation_sauces(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_SAUCES).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocators.CHECK_SECTION_SAUCES))
        check_text = driver.find_element(*TestLocators.CHECK_SECTION_SAUCES).text
        assert check_text == "Соусы"

    def test_check_operation_breads(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_SAUCES).click()
        driver.find_element(*TestLocators.SEARCH_BUTTON_BREADS).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located
                                       (TestLocators.CHECK_SECTION_BREADS))
        check_text = driver.find_element(*TestLocators.CHECK_SECTION_BREADS).text
        assert check_text == "Булки"