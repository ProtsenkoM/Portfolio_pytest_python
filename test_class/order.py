class Order:
    """
    Класс представляет заказ пользователя.
    """
    def __init__(self, user: User, products: list):
        """
        Конструктор для создания заказа.
        """
        pass

    def calculate_total(self) -> float:
        """
        Рассчитывает общую стоимость заказа.
        """
        pass

    def add_product(self, product: Product, quantity: int):
        """
        Добавляет продукт в заказ.
        """
        pass

    def remove_product(self, product: Product):
        """
        Удаляет продукт из заказа.
        """
        pass

    def get_order_summary(self) -> dict:
        """
        Возвращает сводку заказа.
        """
        pass
