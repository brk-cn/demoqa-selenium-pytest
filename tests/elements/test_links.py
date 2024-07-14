from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

def test_links(driver):
    driver.get("https://demoqa.com/elements")
    driver.execute_script("window.scrollBy(0, 100)")
    links_item = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "item-5")))
    links_item.click()
    driver.execute_script("window.scrollBy(0, 250)")

    home_link = driver.find_element(By.ID, "simpleLink")
    home_link.click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == "https://demoqa.com/"
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    dynamic_link = driver.find_element(By.ID, "dynamicLink")
    dynamic_link.click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == "https://demoqa.com/"
    driver.close()
    driver.switch_to.window(driver.window_handles[0])