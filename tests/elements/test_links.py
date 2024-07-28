from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("setup")
class TestLinks:

    def test_simple_link(self):
        self.driver.get("https://demoqa.com/links")

        simple_link = self.driver.find_element(By.ID, "simpleLink")
        simple_link.click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url == "https://demoqa.com/"

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_dynamic_link(self):
        self.driver.get("https://demoqa.com/links")

        dynamic_link = self.driver.find_element(By.ID, "dynamicLink")
        dynamic_link.click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url == "https://demoqa.com/"
        
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
