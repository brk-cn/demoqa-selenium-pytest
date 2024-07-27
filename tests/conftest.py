from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.quit()
