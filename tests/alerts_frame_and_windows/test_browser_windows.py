from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("setup")
class TestBrowserWindows:
    
    def test_new_tab(self):
        self.driver.get("https://demoqa.com/browser-windows")
          
        new_tab_btn = self.driver.find_element(By.ID, "tabButton")
        new_tab_btn.click()
          
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url == "https://demoqa.com/sample", "New Tab Test Failed"
        
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_new_window(self):
        self.driver.get("https://demoqa.com/browser-windows")
        
        new_window_button = self.driver.find_element(By.ID, "windowButton")
        new_window_button.click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url == "https://demoqa.com/sample", "New Window Test Failed"
        
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])