from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.usefixtures("setup")
class TestAlerts:
    def test_alert(self):
        self.driver.get("https://demoqa.com/alerts")
        
        alert_btn = self.driver.find_element(By.ID, "alertButton")
        alert_btn.click()

        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        
        alert_message = alert.text
        alert.accept()

        assert "You clicked a button" in alert_message, "Alert test failed."

    def test_timer_alert(self):
        self.driver.get("https://demoqa.com/alerts")
        
        timer_alert_btn = self.driver.find_element(By.ID, "timerAlertButton")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", timer_alert_btn)
        timer_alert_btn.click()

        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        alert_message = alert.text
        alert.accept()

        assert "This alert appeared after 5 seconds" in alert_message, "Timer alert test failed."

    def test_confirm_alert(self):
        self.driver.get("https://demoqa.com/alerts")
        
        confirm_alert_btn = self.driver.find_element(By.ID, "confirmButton")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", confirm_alert_btn)
        confirm_alert_btn.click()

        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        
        result_text = self.driver.find_element(By.ID, "confirmResult").text
        assert "You selected Ok" in result_text, "Confirm alert test failed."
    
    def test_prompt_alert(self):
        self.driver.get("https://demoqa.com/alerts")
        
        prompt_alert_btn = self.driver.find_element(By.ID, "promtButton")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", prompt_alert_btn)
        prompt_alert_btn.click()

        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        
        alert.send_keys("qwerty")
        alert.accept()

        result_text = self.driver.find_element(By.ID, "promptResult").text
        assert "You entered qwerty" in result_text, "Prompt alert test failed."