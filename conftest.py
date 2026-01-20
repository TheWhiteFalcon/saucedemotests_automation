# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture
def driver():
    """Фикстура для создания драйвера в Docker-окружении."""
    
    # Настройки Chrome
    chrome_options = Options()
    
    # ОБЯЗАТЕЛЬНЫЕ опции для Docker/Selenium Grid
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")  # Режим без графики
    
    # Размер окна
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Подключаемся к Selenium Grid
    # Важно: используем имя сервиса 'selenium', а не localhost
    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        options=chrome_options
    )
    
    yield driver
    
    # Закрываем драйвер после теста
    driver.quit()