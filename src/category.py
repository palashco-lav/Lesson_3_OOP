from abc import ABC, abstractmethod
from typing import List

from src.product import Product


#  исключения, который отвечает за обработку событий,
#  когда в «Категорию» или «Заказ» добавляется товар с нулевым количеством.
class ZeroQuantity(Exception):
    def __init__(self, *args, **kwargs):
        self.message = (
            args[0] if args else "Товар с нулевым количеством не может быть добавлен."
        )

    def __str__(self):
        return self.message


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
    __products: List[Product] = []

    def __init__(self, name: str, description: str, products: Product | List[Product]):
        super().__init__()
        if not isinstance(name, str) or not name:
            raise ValueError("Некорректное название категории")
        self.name = name

        if not isinstance(description, str) or not description:
            raise ValueError("Некорректное описание категории")
        self.description = description

        self.__products = []
        if isinstance(products, list):
            # self.validate_product(p for p in products)
            if any(not isinstance(p, Product) for p in products):
                raise ValueError("Некорректный список продуктов")
            for p in products:
                self.add_product(p)
        elif isinstance(products, Product):
            # self.validate_product(products)
            self.add_product(products)
        elif products is None:
            self.__products = None
        else:
            raise ValueError("Некорректный список продуктов")

        Category.total_categories += 1

    def validate_product(self, product: Product):
        if not isinstance(product, Product):
            raise ValueError("Объект должен быть экземпляром Product")
        if product.quantity == 0:
            raise ZeroQuantity

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
            result = len(self.__products)
            return result

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
        try:
            self.validate_product(product)
        except ZeroQuantity:
            raise ZeroQuantity
        else:
            print(f"Товар добавлен: {product.name}")

        finally:
            Category.total_products += 1
            print(f"Обработка добавления товара завершена")
            # self.__products = products.copy()
            self.__products.append(product)

    def calculate_total(self) -> float:
        return sum(p.quantity for p in self.__products)

    @property
    def display_info(self) -> str:
        return f"{self.name}, количество продуктов: {self.calculate_total()}"

    def middle_price(self) -> float:
        # если кол-во товаров категории нулевое - возвращаю ноль
        if (
            self.__products == None
            or self.__products == []
            or len(self.__products) == 0
        ):
            return 0
        # подсчета среднего ценника всех товаров в классе Category
        # суммарная стоимость всех категорий товаров, делим на кол-во категорий товаров
        return sum(p.price for p in self.__products) / len(self.__products)


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

        self.__products = product
        self.quantity = quantity
        self.__products.quantity -= quantity

    def validate_product(self, product: Product):
        if not hasattr(product, "price"):
            raise AttributeError("Товар должен иметь атрибут 'price'")

    def _validate_quantity(self, product: Product, quantity: int):
        if quantity <= 0 or product.quantity < quantity:
            raise ValueError("Некорректное количество товара")

    def add_product(self, product: Product):
        #
        if not isinstance(product, Product) and not issubclass(
            product.__class__, Product
        ):
            raise ValueError(
                "Продукт должен быть объектом или подклассом класса Product"
            )
        try:
            self.validate_product(product)
        except ZeroQuantity:
            pass
        else:
            print(f"Товар добавлен: {product.name}")

        finally:
            Category.total_products += 1
            print(f"Обработка добавления товара завершена")
        self.__products.append(product)

    def calculate_total(self) -> float:
        return self.__products.price * self.quantity

    @property
    def display_info(self) -> str:
        return f"Заказ: {self.__products.name} × {self.quantity} = {self.calculate_total():.2f} ₽"

    def update_quantity(self, new_quantity: int):
        """Обновление количества с пересчетом суммы"""
        if new_quantity <= 0:
            raise ValueError("Количество должно быть положительным числом")
        self.__products.quantity -= new_quantity - self.quantity
        self.quantity = new_quantity
        self.total = self.calculate_total()

    def __repr__(self):
        return f"Заказ: {self.product} × {self.quantity} = {self.total:.2f} ₽"
