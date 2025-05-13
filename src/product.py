class Product:
    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии

    def __init__(self, name, description, price, quantity):
        # Валидация имени
        if not isinstance(name, str) or not name:
            raise ValueError("Название должно быть непустой строкой")
        self.name = name

        # Валидация описания
        if not isinstance(description, str) or not description:
            raise ValueError("Описание должно быть непустой строкой")
        self.description = description

        # Валидация цены
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Цена должна быть положительным числом")
        self.price = float(price)

        # Валидация количества
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Количество должно быть положительным целым числом")
        self.quantity = quantity
