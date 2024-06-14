from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def test_practice_form(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "firstName")))
    driver.execute_script("window.scrollBy(0, 250)")

    first_name = driver.find_element(By.ID, "firstName")
    first_name.send_keys("John")

    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys("Doe")

    email = driver.find_element(By.ID, "userEmail")
    email.send_keys("johndoe@example.com")

    gender = driver.find_element(By.XPATH, "//label[text()='Male']")
    gender.click()

    mobile_number = driver.find_element(By.ID, "userNumber")
    mobile_number.send_keys("1234567890")

    driver.execute_script("window.scrollBy(0, 200)")

    date_of_birth = driver.find_element(By.ID, "dateOfBirthInput")
    date_of_birth.click()
    date_of_birth.send_keys(Keys.CONTROL + "a")
    date_of_birth.send_keys("01 Jan 2024")
    date_of_birth.send_keys(Keys.ENTER)

    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys("Computer Science")
    subjects.send_keys(Keys.ENTER)

    driver.execute_script("window.scrollBy(0, 200)")

    hobbies = driver.find_elements(By.XPATH, "//label[contains(@for, 'hobbies-checkbox-')]")
    for hobby in hobbies:
        hobby.click()

    address = driver.find_element(By.ID, "currentAddress")
    address.send_keys("My current address")

    state = driver.find_element(By.ID, "react-select-3-input")
    state.send_keys("NCR")
    state.send_keys(Keys.ENTER)

    city = driver.find_element(By.ID, "react-select-4-input")
    city.send_keys("Delhi")
    city.send_keys(Keys.ENTER)

    submit = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].click();", submit)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )

    assert driver.find_element(By.ID, "example-modal-sizes-title-lg").is_displayed()