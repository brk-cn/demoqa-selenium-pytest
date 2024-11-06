from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.usefixtures("setup")
class TestTabs:

    def test_tabs_what(self):
        self.driver.get("https://demoqa.com/tabs")

        what_tab = self.driver.find_element(By.ID, "demo-tab-what")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", what_tab)
        what_tab.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "demo-tabpane-what"))
        )
        what_content = self.driver.find_element(By.ID, "demo-tabpane-what").text
        assert "Lorem Ipsum is simply dummy text" in what_content

    def test_tabs_origin(self):
        self.driver.get("https://demoqa.com/tabs")

        origin_tab = self.driver.find_element(By.ID, "demo-tab-origin")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", origin_tab)
        origin_tab.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "demo-tabpane-origin"))
        )
        origin_content = self.driver.find_element(By.ID, "demo-tabpane-origin").text
        assert "Contrary to popular belief" in origin_content

    def test_tabs_use(self):
        self.driver.get("https://demoqa.com/tabs")

        use_tab = self.driver.find_element(By.ID, "demo-tab-use")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", use_tab)
        use_tab.click()
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "demo-tabpane-use"))
        )
        use_content = self.driver.find_element(By.ID, "demo-tabpane-use").text
        assert "It is a long established fact" in use_content
