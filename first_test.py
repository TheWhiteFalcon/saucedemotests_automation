from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. Настройка драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # 2. Открываем сайт
    driver.get("https://www.saucedemo.com/")
    print("✓ Сайт открылся!")
    
    # 3. Дадим время посмотреть
    time.sleep(3)
    
    # 4. Проверяем заголовок страницы
    page_title = driver.title
    print(f"✓ Заголовок страницы: '{page_title}'")
    
    if "Swag Labs" in page_title:
        print("✓ Открылась правильная страница!")
    else:
        print("✗ Что-то пошло не так...")
        
except Exception as e:
    print(f"✗ Ошибка: {e}")
    
finally:
    # 5. Закрываем браузер
    driver.quit()
    print("✓ Браузер закрыт.")
