from abc import ABC, abstractmethod
from typing import List

from src.product import Product


class BaseEntity(ABC):
    """Абстрактный базовый класс для сущностей работы с продуктами"""

    @abstractmethod
    def validate_product(self, product: "Product"):
        """Валидация продукта перед добавлением"""
        pass

    @abstractmethod
    def calculate_total(self) -> float:
        """Расчет общей метрики (стоимость/количество)"""
        pass

    @property
    @abstractmethod
    def display_info(self) -> str:
        """Строковое представление информации"""
        pass


class Category(BaseEntity):
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: Product | List[Product]):
        super().__init__()
        if not isinstance(name, str) or not name:
            raise ValueError("Некорректное название категории")
        self.name = name

        if not isinstance(description, str) or not description:
            raise ValueError("Некорректное описание категории")
        self.description = description

        if isinstance(products, list):
            if any(not isinstance(p, Product) for p in products):
                raise ValueError("Некорректный список продуктов")
            self.__products = products.copy()
            Category.total_products += len(self.__products)
        elif isinstance(products, Product):
            self.__products = products
            Category.total_products += 1
        elif products is None:
            self.__products = None
        else:
            raise ValueError("Некорректный список продуктов")

        Category.total_categories += 1

    def validate_product(self, product: Product):
        if not isinstance(product, Product):
            raise ValueError("Объект должен быть экземпляром Product")

    def __str__(self):
        sum_products = 0
        # Суммирую общее кол-во продуктов
        for product in self.__products:
            sum_products += product.quantity
        # Название категории, количество продуктов: 200 шт.
        return f"{self.name}, количество продуктов: {sum_products}"

    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += product.__str__() + "\n"
        return result

    @property
    def category_count(self):
        return self.total_categories

    @property
    def product_count(self):
        return self.total_products

    @property
    def category_product_count(self):
        if self.__products is None:
            return 0
        else:
            return len(self.__products)

    @property
    def get_product_info(self):
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    def add_product(self, product: Product):
        #
        if not isinstance(product, Product) and not issubclass(
            product.__class__, Product
        ):
            raise ValueError(
                "Продукт должен быть объектом или подклассом класса Product"
            )
        self.__products.append(product)
        Category.total_products += 1

    def calculate_total(self) -> float:
        return sum(p.quantity for p in self.__products)

    @property
    def display_info(self) -> str:
        return f"{self.name}, количество продуктов: {self.calculate_total()}"


class CategoryIterator:
    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category._Category__products):
            product = self.category._Category__products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


class Order(BaseEntity):
    def __init__(self, product: Product, quantity: int):
        self.validate_product(product)
        self._validate_quantity(product, quantity)

        self.product = product
        self.quantity = quantity
        self.product.quantity -= quantity

    def validate_product(self, product: Product):
        if not hasattr(product, "price"):
            raise AttributeError("Товар должен иметь атрибут 'price'")

    def _validate_quantity(self, product: Product, quantity: int):
        if quantity <= 0 or product.quantity < quantity:
            raise ValueError("Некорректное количество товара")

    def calculate_total(self) -> float:
        return self.product.price * self.quantity

    @property
    def display_info(self) -> str:
        return f"Заказ: {self.product.name} × {self.quantity} = {self.calculate_total():.2f} ₽"

    def update_quantity(self, new_quantity: int):
        """Обновление количества с пересчетом суммы"""
        if new_quantity <= 0:
            raise ValueError("Количество должно быть положительным числом")
        self.product.quantity -= new_quantity - self.quantity
        self.quantity = new_quantity
        self.total = self.calculate_total()

    def __repr__(self):
        return f"Заказ: {self.product} × {self.quantity} = {self.total:.2f} ₽"
