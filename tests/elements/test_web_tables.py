from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_check_box(driver):
    driver.get("https://demoqa.com/elements")

    web_tables_item = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "item-3")))
    web_tables_item.click()
    driver.execute_script("window.scrollBy(0, 250)")

    driver.find_element(By.ID, "addNewRecordButton").click()

    expected_first_name = "John"
    expected_last_name = "Doe"
    expected_email = "johndoe@example.com"
    expected_age = "30"
    expected_salary = "100000"
    expected_department = "Engineering"

    driver.find_element(By.ID, "firstName").send_keys(expected_first_name)
    driver.find_element(By.ID, "lastName").send_keys(expected_last_name)
    driver.find_element(By.ID, "userEmail").send_keys(expected_email)
    driver.find_element(By.ID, "age").send_keys(expected_age)
    driver.find_element(By.ID, "salary").send_keys(expected_salary)
    driver.find_element(By.ID, "department").send_keys(expected_department)

    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()

    rows = driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
    for row in rows:
        cells = row.find_elements(By.CSS_SELECTOR, ".rt-td")
        if len(cells) > 0 and cells[0].text == expected_first_name and cells[1].text == expected_last_name:
            assert cells[2].text == expected_age
            assert cells[3].text == expected_email
            assert cells[4].text == expected_salary
            assert cells[5].text == expected_department
