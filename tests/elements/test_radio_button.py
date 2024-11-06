
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.usefixtures("setup")
class TestRadioButton:

    def test_radio_button_yes(self):
        self.driver.get("https://demoqa.com/radio-button")

        yes_radio_label = self.driver.find_element(By.XPATH, "//label[@for='yesRadio']")
        self.driver.execute_script("arguments[0].click();", yes_radio_label)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-success")))
        spans = self.driver.find_elements(By.CLASS_NAME, "text-success")
        actual_value = spans[0].text.strip()

        assert actual_value == "Yes"

    def test_radio_button_impressive(self):
        self.driver.get("https://demoqa.com/radio-button")

        impressive_radio_label = self.driver.find_element(By.XPATH, "//label[@for='impressiveRadio']")
        self.driver.execute_script("arguments[0].click();", impressive_radio_label)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-success")))
        spans = self.driver.find_elements(By.CLASS_NAME, "text-success")
        actual_value = spans[0].text.strip()

        assert actual_value == "Impressive"

    def test_radio_button_no(self):
        self.driver.get("https://demoqa.com/radio-button")

        no_radio_input = self.driver.find_element(By.ID, "noRadio")

        assert not no_radio_input.is_enabled()