from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_check_box(driver):
    driver.get("https://demoqa.com/elements")

    wait = WebDriverWait(driver, 10)
    radio_button_item = wait.until(EC.element_to_be_clickable((By.ID, "item-2")))
    radio_button_item.click()
    driver.execute_script("window.scrollBy(0, 250)")

    yes_radio_label = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    yes_radio_label.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "text-success")))
    spans = driver.find_elements(By.CLASS_NAME, "text-success")
    actual_value = spans[0].text.strip()
    print(actual_value)
    
    assert actual_value == "Yes", f"Expected value: Yes, Actual value: {actual_value}"

    impressive_radio_label = driver.find_element(By.XPATH, "//label[@for='impressiveRadio']")
    impressive_radio_label.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "text-success")))
    spans = driver.find_elements(By.CLASS_NAME, "text-success")
    actual_value = spans[0].text.strip()

    assert actual_value == "Impressive", f"Expected value: Impressive, Actual value: {actual_value}"
