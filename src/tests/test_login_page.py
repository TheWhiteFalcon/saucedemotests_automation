import pytest
import allure
from src.pages.login_page import LoginPage


@allure.epic("Sauce Demo Tests")
@allure.feature("Авторизация")
class TestLogin:
    
    @allure.title("Тест 1: Открытие страницы логина")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_login_page(self, login_page):
        with allure.step("Проверяем заголовок страницы"):
            title = login_page.get_title()
            assert "Swag Labs" in title
            allure.attach(title, "Фактический заголовок", allure.attachment_type.TEXT)
    
    @allure.title("Тест 2: Успешный логин (standard_user)")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_with_valid_credentials(self, login_page):
        with allure.step("Вводим логин и пароль standard_user"):
            login_page.login(username="standard_user", password="secret_sauce")
        
        with allure.step("Проверяем URL страницы товаров"):
            assert "inventory" in login_page.driver.current_url
            allure.attach(login_page.driver.current_url, "Текущий URL", allure.attachment_type.TEXT)
    
    @allure.title("Тест 3: Логин с неверным паролем")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_invalid_password(self, login_page):
        with allure.step("Вводим неверный пароль"):
            login_page.login(username="standard_user", password="wrong_password")
        
        with allure.step("Проверяем сообщение об ошибке"):
            error_text = login_page.get_error_message()
            assert "Username and password do not match" in error_text
            allure.attach(error_text, "Текст ошибки", allure.attachment_type.TEXT)
    
    @allure.title("Тест 4: Логин заблокированного пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_locked_out_user(self, login_page):
        with allure.step("Пытаемся войти как locked_out_user"):
            login_page.login(username="locked_out_user", password="secret_sauce")
        
        with allure.step("Проверяем сообщение о блокировке"):
            error_text = login_page.get_error_message()
            assert "Sorry, this user has been locked out" in error_text
    
    @allure.title("Тест 5: Логин с пустыми полями")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_empty_fields(self, login_page):
        with allure.step("Нажимаем Login без заполнения полей"):
            login_page.click_login()
        
        with allure.step("Проверяем сообщение о необходимости username"):
            error_text = login_page.get_error_message()
            assert "Username is required" in error_text
    
    @allure.title("Тест 6: Логин performance_glitch_user")
    @allure.severity(allure.severity_level.MINOR)
    def test_login_performance_glitch_user(self, login_page):
        import time
        
        with allure.step("Замеряем время входа"):
            start_time = time.time()
            login_page.login(username="performance_glitch_user", password="secret_sauce")
            end_time = time.time()
            load_time = end_time - start_time
            
            allure.attach(str(load_time), f"Время загрузки: {load_time:.2f} сек", allure.attachment_type.TEXT)
        
        with allure.step("Проверяем успешный вход"):
            assert "inventory" in login_page.driver.current_url
            assert "Products" in login_page.driver.page_source
