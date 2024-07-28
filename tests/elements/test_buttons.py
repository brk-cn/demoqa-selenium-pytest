from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest

@pytest.mark.usefixtures("setup")
class TestButtons:

    def test_double_click_me(self):
        self.driver.get("https://demoqa.com/buttons")

        actions = ActionChains(self.driver)

        double_click_btn = self.driver.find_element(By.ID, 'doubleClickBtn')
        actions.double_click(double_click_btn).perform()

        double_click_message = self.driver.find_element(By.ID, 'doubleClickMessage').text
        assert double_click_message == "You have done a double click"

    def test_right_click_me(self):
        self.driver.get("https://demoqa.com/buttons")

        actions = ActionChains(self.driver)

        right_click_btn = self.driver.find_element(By.ID, 'rightClickBtn')
        actions.context_click(right_click_btn).perform()

        right_click_message = self.driver.find_element(By.ID, 'rightClickMessage').text
        assert right_click_message == "You have done a right click"

    def test_click_me(self):
        self.driver.get("https://demoqa.com/buttons")

        click_me_btn = self.driver.find_element(By.XPATH, '//button[text()="Click Me"]')
        click_me_btn.click()

        click_me_message = self.driver.find_element(By.ID, 'dynamicClickMessage').text
        assert click_me_message == "You have done a dynamic click"