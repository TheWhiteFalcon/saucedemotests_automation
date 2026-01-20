class BasePage:
    """Базовый класс для всех страниц. Здесь будет общая логика."""
    
    def __init__(self, driver):
        """Конструктор. Принимает драйвер и сохраняет его."""
        self.driver = driver

    def find_element(self, locator):
        """Найти один элемент на странице по локатору."""
        # Пока упрощённая версия, позже добавим ожидания
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """Найти все элементы по локатору."""
        return self.driver.find_elements(*locator)

    def get_title(self):
        """Получить заголовок страницы."""
        return self.driver.title
