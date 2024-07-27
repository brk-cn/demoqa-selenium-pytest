from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("setup")
class TestHomePage:
    
    def test_homepage_title(self):
        self.driver.get("https://demoqa.com")
        assert self.driver.title == "DEMOQA"
  
    def test_navigation_to_elements_page(self):
        self.driver.get("https://demoqa.com")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]').click()
        assert "elements" in self.driver.current_url

    def test_navigation_to_forms_page(self):
        self.driver.get("https://demoqa.com")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[2]').click()
        assert "forms" in self.driver.current_url

    def test_navigation_to_alerts_frame_and_windows_page(self):
        self.driver.get("https://demoqa.com")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[3]').click()
        assert "alertsWindows" in self.driver.current_url

    def test_navigation_to_widgets_page(self):
        self.driver.get("https://demoqa.com")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[4]').click()
        assert "widgets" in self.driver.current_url

    def test_navigation_to_interactions_page(self):
        self.driver.get("https://demoqa.com")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[5]').click()
        assert "interaction" in self.driver.current_url

    def test_navigation_to_book_store_application_page(self):
        self.driver.get("https://demoqa.com")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[6]').click()
        assert "books" in self.driver.current_url
