from test.locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSectionConstructor:
    def test_check_operation_fillings(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_FILLINGS).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element(
                TestLocators.CHECK_SECTION_FILLINGS, "Начинки"
            )
        )

        check_text = driver.find_element(*TestLocators.CHECK_SECTION_FILLINGS).text
        assert check_text == "Начинки"

    def test_check_operation_sauces(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_SAUCES).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element(
                TestLocators.CHECK_SECTION_SAUCES, "Соусы"
            )
        )
        check_text = driver.find_element(*TestLocators.CHECK_SECTION_SAUCES).text
        assert check_text == "Соусы"

    def test_check_operation_breads(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_SAUCES).click()
        driver.find_element(*TestLocators.SEARCH_BUTTON_BREADS).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element(
                TestLocators.CHECK_SECTION_BREADS, "Булки"
            )
        )
        check_text = driver.find_element(*TestLocators.CHECK_SECTION_BREADS).text
        assert check_text == "Булки"
