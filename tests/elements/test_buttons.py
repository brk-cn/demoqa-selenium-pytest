from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def test_buttons(driver):
    driver.get("https://demoqa.com/elements")

    buttons_item = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "item-4")))
    buttons_item.click()
    driver.execute_script("window.scrollBy(0, 250)")

    actions = ActionChains(driver)

    double_click_btn = driver.find_element(By.ID, 'doubleClickBtn')
    actions.double_click(double_click_btn).perform()

    right_click_btn = driver.find_element(By.ID, 'rightClickBtn')
    actions.context_click(right_click_btn).perform()

    click_me_btn = driver.find_element(By.XPATH, '//button[text()="Click Me"]')
    click_me_btn.click()

    double_click_message = driver.find_element(By.ID, 'doubleClickMessage').text
    right_click_message = driver.find_element(By.ID, 'rightClickMessage').text
    click_me_message = driver.find_element(By.ID, 'dynamicClickMessage').text

    assert double_click_message == "You have done a double click", "Double Click Test Failed"
    assert right_click_message == "You have done a right click", "Right Click Test Failed"
    assert click_me_message == "You have done a dynamic click", "Click Me Test Failed"