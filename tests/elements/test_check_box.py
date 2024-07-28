from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.usefixtures("setup")
class TestCheckBox:

    def test_check_box_all_checked(self):
        self.driver.get("https://demoqa.com/checkbox")

        self.driver.find_element(By.XPATH, "//label[@for='tree-node-home']").click()

        result_div = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "result")))
        selected_items = result_div.find_elements(By.CLASS_NAME, "text-success")

        expected_items = [
            "home",
            "desktop",
            "notes",
            "commands",
            "documents",
            "workspace",
            "react",
            "angular",
            "veu",
            "office",
            "public",
            "private",
            "classified",
            "general",
            "downloads",
            "wordFile",
            "excelFile"
        ]

        actual_items = [item.text for item in selected_items]

        assert actual_items == expected_items