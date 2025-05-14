class Product:
    name: str  # название
    description: str  # описание
    __price: float  # цена
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
        if not isinstance(price, (int, float)) or price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        self.__price = float(price)

        # Валидация количества
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Количество должно быть положительным целым числом")
        self.quantity = quantity

    def __str__(self) -> str:
        # Название продукта, 80 руб. Остаток: 15 шт.
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity}"

    def __add__(self, other):
        return self.quantity * self.__price + other.quantity * other.__price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, (int, float)) or new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            user_input = input(
                "Цена товара будет понижена. Подтвердите действие (y/n): "
            )
            if user_input.lower() == "y":
                self.__price = new_price
            else:
                print("Понижение цены отменено.")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict, products=None):
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")

        if products:
            for product in products:
                if product.name == name:
                    # Если товар с таким именем уже существует, обновляем его параметры
                    product.quantity += quantity
                    if price > product.price:
                        product.price = price
                    return product

        return cls(name, description, price, quantity)
