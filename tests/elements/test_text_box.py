from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_text_box(driver):
    driver.get("https://demoqa.com/elements")

    wait = WebDriverWait(driver, 10)
    text_box_item = wait.until(EC.element_to_be_clickable((By.ID, "item-0")))
    text_box_item.click()

    name_field = driver.find_element(By.ID, "userName")
    email_field = driver.find_element(By.ID, "userEmail")
    current_address_field = driver.find_element(By.ID, "currentAddress")
    permanent_address_field = driver.find_element(By.ID, "permanentAddress")

    expected_name = "John Doe"
    expected_email = "johndoe@example.com"
    expected_current_address = "123 ABC"
    expected_permanent_address = "456 DEF"

    name_field.send_keys(expected_name)
    email_field.send_keys(expected_email)
    current_address_field.send_keys(expected_current_address)
    permanent_address_field.send_keys(expected_permanent_address)

    driver.execute_script("window.scrollBy(0, 500)")
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    output_div = driver.find_element(By.ID, "output")
    actual_name = output_div.find_element(By.ID, "name").text.split(":")[1]
    actual_email = output_div.find_element(By.ID, "email").text.split(":")[1]
    actual_current_address = output_div.find_element(By.ID, "currentAddress").text.split(":")[1]
    actual_permanent_address = output_div.find_element(By.ID, "permanentAddress").text.split(":")[1]

    assert actual_name == expected_name, "Username could not be verified"
    assert actual_email == expected_email, "Email could not be verified"
    assert actual_current_address == expected_current_address, "Current address could not be verified"
    assert actual_permanent_address == expected_permanent_address, "Permanent address could not be verified"
