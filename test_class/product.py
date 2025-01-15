class Product:
    """
    Класс представляет продукт в системе.
    """
    def __init__(self, name: str, price: float, stock: int):
        """
        Конструктор для создания объекта продукта.
        """
        pass

    def update_stock(self, quantity: int):
        """
        Изменяет количество товара на складе.
        """
        pass

    def apply_discount(self, discount_percentage: float):
        """
        Применяет скидку к цене продукта.
        """
        pass

    def get_product_details(self) -> dict:
        """
        Возвращает информацию о продукте в виде словаря.
        """
        pass
