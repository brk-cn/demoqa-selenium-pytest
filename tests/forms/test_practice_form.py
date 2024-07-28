from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.mark.usefixtures("setup")
class TestPracticeForm:
    
    def test_submit_form(self):
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.driver.execute_script(f"window.scrollBy(0, 750);")
        
        self.driver.find_element(By.ID, "firstName").send_keys("John")
        self.driver.find_element(By.ID, "lastName").send_keys("Doe")
        self.driver.find_element(By.ID, "userEmail").send_keys("johndoe@example.com")
        self.driver.find_element(By.XPATH, "//label[contains(text(),'Male')]").click()
        self.driver.find_element(By.ID, "userNumber").send_keys("1234567890")

        subjects_input = self.driver.find_element(By.ID, "subjectsInput")
        subjects_input.send_keys("Computer")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "react-select-2-option-0")))
        subjects_input.send_keys(Keys.ARROW_DOWN)
        subjects_input.send_keys(Keys.ENTER)

        hobbies_checkbox = self.driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']")
        self.driver.execute_script("arguments[0].click();", hobbies_checkbox)
        hobbies_checkbox = self.driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-2']")
        self.driver.execute_script("arguments[0].click();", hobbies_checkbox)
        hobbies_checkbox = self.driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-3']")
        self.driver.execute_script("arguments[0].click();", hobbies_checkbox)

        self.driver.find_element(By.ID, "currentAddress").send_keys("123 ABC")
        
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(By.ID, "state"))
        self.driver.find_element(By.ID, "state").click()
        self.driver.find_element(By.XPATH, "//div[contains(text(),'NCR')]").click()
        
        self.driver.find_element(By.ID, "city").click()
        self.driver.find_element(By.XPATH, "//div[contains(text(),'Delhi')]").click()

        self.driver.find_element(By.ID, "submit").click()

        confirmation_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
        ).text

        assert "Thanks for submitting the form" in confirmation_message
