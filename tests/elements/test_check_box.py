from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_check_box(driver):
    driver.get("https://demoqa.com/elements")

    check_box_item = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "item-1")))
    check_box_item.click()

    expand_button = driver.find_element(By.CLASS_NAME, "rct-option-expand-all")
    expand_button.click()

    label_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-home']")
    label_checkbox.click()
    
    result_div = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "result")))
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

    assert actual_items == expected_items, f"Expected items: {expected_items}, Actual items: {actual_items}"