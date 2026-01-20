# src/pages/inventory_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    """Page Object для страницы с товарами после успешного логина."""
    
    # Локаторы
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    
    def __init__(self, driver):
        super().__init__(driver)
        # Проверяем, что мы на правильной странице
        assert "inventory" in driver.current_url
        assert self.is_products_title_displayed()
    
    def is_products_title_displayed(self):
        """Проверяет, отображается ли заголовок 'Products'."""
        try:
            return self.find_element(self.PRODUCTS_TITLE).is_displayed()
        except:
            return False
    
    def get_title_text(self):
        """Возвращает текст заголовка."""
        return self.find_element(self.PRODUCTS_TITLE).text
    
    def get_product_count(self):
        """Возвращает количество товаров на странице."""
        items = self.find_elements((By.CLASS_NAME, "inventory_item"))
        return len(items)
