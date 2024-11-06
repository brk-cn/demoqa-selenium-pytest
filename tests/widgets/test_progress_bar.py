from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.usefixtures("setup")
class TestProgressBar:

    def test_progress_bar_complete(self):
        self.driver.get("https://demoqa.com/progress-bar")

        start_button = self.driver.find_element(By.ID, "startStopButton")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", start_button)
        start_button.click()

        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "progress-bar"), "100%")
        )

        progress_bar = self.driver.find_element(By.CLASS_NAME, "progress-bar")
        assert "100%" in progress_bar.text