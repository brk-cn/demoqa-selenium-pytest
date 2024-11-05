from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.usefixtures("setup")
class TestAccordion:

    def test_accordion_section_1(self):
        self.driver.get("https://demoqa.com/accordian")

        section_1_content = self.driver.find_element(By.ID, "section1Content")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", section_1_content)

        content_text = section_1_content.text
        assert "Lorem Ipsum is simply dummy text" in content_text

    def test_accordion_section_2(self):
        self.driver.get("https://demoqa.com/accordian")
        
        section_2_header = self.driver.find_element(By.ID, "section2Heading")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", section_2_header)
        section_2_header.click()

        section_2_content = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "section2Content"))
        )
        content_text = section_2_content.text
        assert "Contrary to popular belief" in content_text

    def test_accordion_section_3(self):
        self.driver.get("https://demoqa.com/accordian")
        
        section_3_header = self.driver.find_element(By.ID, "section3Heading")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", section_3_header)
        section_3_header.click()

        section_3_content = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "section3Content"))
        )
        content_text = section_3_content.text
        assert "It is a long established fact" in content_text
