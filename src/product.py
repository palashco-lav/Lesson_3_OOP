class Product:
    name: str  # название
    description: str  # описание
    __price: float  # цена
    quantity: int  # количество в наличии

    def __init__(self, name: str, description: str, price: float, quantity: int):
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

        if not isinstance(name, str) or not name:
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(description, str) or not description:
            raise ValueError("Описание должно быть непустой строкой")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Количество должно быть положительным целым числом")

        if products:
            for product in products:
                if product.name == name:
                    # Если товар с таким именем уже существует, обновляем его параметры
                    product.quantity += quantity
                    if price > product.price:
                        product.price = price
                    return product

        return cls(name, description, price, quantity)


class Smartphone(Product):
    efficiency: float  # производительность
    model: str  # модель
    memory: int  # объем встроенной памяти
    color: str  # цвет

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        # Валидация производительности
        if not isinstance(efficiency, float) or efficiency <= 0:
            raise ValueError(
                "Производительность должна быть не отрицательная переменная с плавающей точкой"
            )
        self.efficiency = efficiency

        # Валидация модели
        if not isinstance(model, str) or not model:
            raise ValueError("Описание должно быть непустой строкой")
        self.model = model

        # Валидация объёма встроенной памяти
        if not isinstance(memory, int) or memory < 0:
            raise ValueError("Объём памяти должен быть целочисленным больше нуля")
        self.memory = memory

        # Валидация цвета
        if not isinstance(color, str) or not color:
            raise ValueError("Цвет должен быть непустой строкой")
        self.color = color

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError(
                f"Для сложения типы переменных должны совпадать {type(self)} != {type(other)}"
            )
        return self.quantity * self.__price + other.quantity * other.__price


class LawnGrass(Product):
    country: str  # страна-производитель
    germination_period: int  # срок прорастания
    color: str  # цвет

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        # Валидация страны производителя
        if not isinstance(country, str) or not country:
            raise ValueError("Страна-производитель должена быть непустой строкой")
        self.country = country
        # Валидация срока прорастания
        if not isinstance(germination_period, int) or germination_period < 0:
            raise ValueError(
                "Срок прорастания должен быть целочисленной переменной больше нуля"
            )
        self.germination_period = germination_period
        # Валидация цвета
        if not isinstance(color, str) or not color:
            raise ValueError("Цвет должен быть непустой строкой")
        self.color = color

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError(
                f"Для сложения типы переменных должны совпадать {type(self)} != {type(other)}"
            )
        return self.quantity * self.__price + other.quantity * other.__price
