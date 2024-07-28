from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("setup")
class TestTextBox:

    def test_text_box(self):
        self.driver.get("https://demoqa.com/text-box")

        expected_name = "John Doe"
        expected_email = "johndoe@example.com"
        expected_current_address = "123 ABC"
        expected_permanent_address = "456 DEF"

        self.driver.find_element(By.ID, "userName").send_keys(expected_name)
        self.driver.find_element(By.ID, "userEmail").send_keys(expected_email)
        self.driver.find_element(By.ID, "currentAddress").send_keys(expected_current_address)
        self.driver.find_element(By.ID, "permanentAddress").send_keys(expected_permanent_address)

        self.driver.execute_script("window.scrollBy(0, 500)")
        self.driver.find_element(By.ID, "submit").click()

        output_div = self.driver.find_element(By.ID, "output")
        actual_name = output_div.find_element(By.ID, "name").text.split(":")[1]
        actual_email = output_div.find_element(By.ID, "email").text.split(":")[1]
        actual_current_address = output_div.find_element(By.ID, "currentAddress").text.split(":")[1]
        actual_permanent_address = output_div.find_element(By.ID, "permanentAddress").text.split(":")[1]

        assert expected_name == actual_name
        assert expected_email == actual_email
        assert expected_current_address == actual_current_address
        assert expected_permanent_address == actual_permanent_address