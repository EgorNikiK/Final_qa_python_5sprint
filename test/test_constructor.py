from test.locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSectionConstructor:
    def test_check_operation_fillings(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_FILLINGS).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.CHECK_SECTION_FILLINGS))
        fillings_section = driver.find_element(*TestLocators.CHECK_SECTION_FILLINGS)
        assert fillings_section.is_displayed(), "Секция 'Начинки' не отображается"

    def test_check_operation_sauces(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_SAUCES).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element(
                TestLocators.CHECK_SECTION_SAUCES))
        sauces_section = driver.find_element(*TestLocators.CHECK_SECTION_SAUCES)
        assert sauces_section.is_displayed(), "Секция 'Соусы' не отображается"

    def test_check_operation_breads(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_SAUCES).click()
        driver.find_element(*TestLocators.SEARCH_BUTTON_BREADS).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element(
                TestLocators.CHECK_SECTION_BREADS ))
        breads_section = driver.find_element(*TestLocators.CHECK_SECTION_BREADS)
        assert breads_section.is_displayed(), "Секция 'Булки' не отображается"
