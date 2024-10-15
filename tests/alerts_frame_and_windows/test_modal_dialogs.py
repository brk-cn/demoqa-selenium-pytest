from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.usefixtures("setup")
class TestModalDialogs:
    
    def test_small_modal(self):
        self.driver.get("https://demoqa.com/modal-dialogs")
        
        small_modal_btn = self.driver.find_element(By.ID, "showSmallModal")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", small_modal_btn)
        small_modal_btn.click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-sm")))
        
        modal_title = self.driver.find_element(By.ID, "example-modal-sizes-title-sm").text
        close_btn = self.driver.find_element(By.ID, "closeSmallModal")
        close_btn.click()

        assert modal_title == "Small Modal", "Small Modal title is incorrect"

    def test_large_modal(self):
        self.driver.get("https://demoqa.com/modal-dialogs")
        
        large_modal_btn = self.driver.find_element(By.ID, "showLargeModal")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", large_modal_btn)
        large_modal_btn.click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))
        
        modal_title = self.driver.find_element(By.ID, "example-modal-sizes-title-lg").text
        close_btn = self.driver.find_element(By.ID, "closeLargeModal")
        close_btn.click()

        assert modal_title == "Large Modal", "Large Modal title is incorrect"
