from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_form_submission(driver):
    driver.get("http://127.0.0.1:8000/index.html")  # для локального теста
    assert "Тестовая Форма" in driver.title

    driver.find_element(By.ID, "name").send_keys("Тестовый Пользователь")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "message").send_keys("Тестовое сообщение")
    driver.find_element(By.TAG_NAME, "button").click()
    
    result = driver.find_element(By.ID, "result").text
    assert "Спасибо, Тестовый Пользователь" in result