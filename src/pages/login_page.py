from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    """Page Object для страницы логина saucedemo.com"""
    
    # ЛОКАТОРЫ (координаты элементов на странице)
    USERNAME_FIELD = (By.ID, 'user-name')        # Поле "Username"
    PASSWORD_FIELD = (By.ID, 'password')         # Поле "Password"
    LOGIN_BUTTON = (By.ID, 'login-button')       # Кнопка "Login"
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]') # Блок с ошибкой
    
    def __init__(self, driver):
        """Открывает страницу логина при создании объекта."""
        super().__init__(driver)  # Вызываем конструктор родителя
        driver.get('https://www.saucedemo.com/')

    def enter_username(self, username):
        """Ввести имя пользователя."""
        username_field = self.find_element(self.USERNAME_FIELD)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        """Ввести пароль."""
        password_field = self.find_element(self.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        """Нажать кнопку Login."""
        self.find_element(self.LOGIN_BUTTON).click()

    def get_error_message(self):
        try:
            # Ждём появления элемента с ошибкой (максимум 5 секунд)
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            
            wait = WebDriverWait(self.driver, 5)
            error_element = wait.until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return error_element.text
        except:
            return ""  # Если элемента с ошибкой нет, возвращаем пустую строку

    def login(self, username, password):
        """Упрощённый метод для полного входа."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
