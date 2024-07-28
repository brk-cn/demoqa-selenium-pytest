from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.usefixtures("setup")
class TestWebTables:

    def test_add_row_to_table(self):
        self.driver.get("https://demoqa.com/webtables")
        
        add_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "addNewRecordButton")))
        add_button.click()
        
        self.driver.find_element(By.ID, "firstName").send_keys("John")
        self.driver.find_element(By.ID, "lastName").send_keys("Doe")
        self.driver.find_element(By.ID, "userEmail").send_keys("johndoe@example.com")
        self.driver.find_element(By.ID, "age").send_keys("25")
        self.driver.find_element(By.ID, "salary").send_keys("50000")
        self.driver.find_element(By.ID, "department").send_keys("IT")
        
        self.driver.find_element(By.ID, "submit").click()
        
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='rt-tbody']")))

        rows = self.driver.find_elements(By.XPATH, "//div[@class='rt-tbody']/div")
        new_row = [row.text for row in rows if "johndoe@example.com" in row.text]
        assert len(new_row) > 0

    def test_edit_row_in_table(self):
        self.driver.get("https://demoqa.com/webtables")
        
        edit_button = self.driver.find_element(By.ID, "edit-record-1")
        edit_button.click()

        self.driver.find_element(By.ID, "firstName").clear()
        self.driver.find_element(By.ID, "firstName").send_keys("Jane")
        self.driver.find_element(By.ID, "lastName").clear()
        self.driver.find_element(By.ID, "lastName").send_keys("Doe")
        self.driver.find_element(By.ID, "userEmail").clear()
        self.driver.find_element(By.ID, "userEmail").send_keys("janedoe@example.com")

        self.driver.find_element(By.ID, "submit").click()
        
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='rt-tbody']")))

        updated_row_data = self.driver.find_element(By.XPATH, "//div[@class='rt-tr-group'][1]//div[@class='rt-td'][4]").text
        assert "janedoe@example.com" in updated_row_data

    def test_delete_rows_from_table(self):
        self.driver.get("https://demoqa.com/webtables")

        self.driver.find_element(By.ID, "delete-record-1").click()
        self.driver.find_element(By.ID, "delete-record-2").click()
        self.driver.find_element(By.ID, "delete-record-3").click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='rt-noData']")))

        no_data_element = self.driver.find_element(By.XPATH, "//div[@class='rt-noData']")
        assert no_data_element.text == "No rows found", f"Expected 'No rows found' message, but got: {no_data_element.text}"

    def test_search_in_table(self):
        self.driver.get("https://demoqa.com/webtables")
    
        search_box = self.driver.find_element(By.ID, "searchBox")
        search_box.send_keys("legal")
    
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='rt-tbody']")))

        rows = self.driver.find_elements(By.XPATH, "//div[@class='rt-tr-group']")
        filtered_rows = [row.text for row in rows if "legal" in row.text.lower()]
        assert len(filtered_rows) > 0