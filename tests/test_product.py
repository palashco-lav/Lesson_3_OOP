import sys
from io import StringIO
from unittest.mock import patch

from src.product import (BaseProduct, LawnGrass, LoggingMixin, Product,
                         Smartphone)


def test_product_init():
    # Создаем тестовый продукт
    product = Product(
        name="iPhone 14", description="Смартфон Apple", price=79990.0, quantity=10
    )

    # Проверяем корректность инициализации
    assert product.name == "iPhone 14"
    assert product.description == "Смартфон Apple"
    assert product.price == 79990.0
    test = product.quantity
    assert test == 10


def test_invalid_name():
    # Проверяем валидацию имени
    try:
        Product(123, "Описание", 100.0, 5)
        assert False, "Должна быть ошибка при неверном типе имени"
    except ValueError:
        pass

    try:
        Product("", "Описание", 100.0, 5)
        assert False, "Должна быть ошибка при пустом имени"
    except ValueError:
        pass


def test_invalid_description():
    # Проверяем валидацию описания
    try:
        Product("Продукт", 123, 100.0, 5)
        assert False, "Должна быть ошибка при неверном типе описания"
    except ValueError:
        pass

    try:
        Product("Продукт", "", 100.0, 5)
        assert False, "Должна быть ошибка при пустом описании"
    except ValueError:
        pass


def test_invalid_price():
    # Проверяем валидацию цены
    try:
        Product("Продукт", "Описание", "сто рублей", 5)
        assert False, "Должна быть ошибка при неверном типе цены"
    except ValueError:
        pass

    try:
        Product("Продукт", "Описание", -100.0, 5)
        assert False, "Должна быть ошибка при отрицательной цене"
    except ValueError:
        pass


def test_invalid_quantity():
    # Проверяем валидацию количества
    try:
        Product("Продукт", "Описание", 100.0, "пять")
        assert False, "Должна быть ошибка при неверном типе количества"
    except ValueError:
        pass

    try:
        Product("Продукт", "Описание", 100.0, -5)
        assert False, "Должна быть ошибка при отрицательном количестве"
    except ValueError:
        pass


def test_change_attributes():
    # Создаем продукт для проверки изменения атрибутов
    product = Product(
        name="iPhone 14", description="Смартфон Apple", price=79990.0, quantity=10
    )

    # Изменяем атрибуты
    product.name = "iPhone 14 Pro"
    product.description = "Флагманский смартфон Apple"
    product.price = 99990.0
    product.quantity = 5

    # Проверяем измененные значения
    assert product.name == "iPhone 14 Pro"
    assert product.description == "Флагманский смартфон Apple"
    assert product.price == 99990.0
    assert product.quantity == 5


def test_new_product():
    # Создаём список товаров для проверки наличия дубликатов
    existing_products = [
        Product("Keyboard", "Gaming keyboard", 100.0, 10),
        Product("Mouse", "Gaming mouse", 50.0, 5),
    ]

    # Проверяем создание нового товара без дубликатов
    new_product = Product.new_product(
        {
            "name": "Headphones",
            "description": "Gaming headphones",
            "price": 80.0,
            "quantity": 7,
        }
    )
    assert new_product.name == "Headphones"
    assert new_product.description == "Gaming headphones"
    assert new_product.price == 80.0
    assert new_product.quantity == 7

    # Проверяем обновление существующего товара
    updated_product = Product.new_product(
        {
            "name": "Keyboard",
            "description": "Gaming keyboard",
            "price": 120.0,
            "quantity": 3,
        },
        existing_products,
    )
    assert updated_product.name == "Keyboard"
    assert updated_product.description == "Gaming keyboard"
    assert updated_product.price == 120.0  # Цена должна быть обновлена до более высокой
    assert updated_product.quantity == 13  # Количество должно быть суммировано


def test_lower_price():
    # Создаём экземпляр класса Product
    product = Product("Смартфон", "Современный смартфон с большим экраном", 1000.0, 10)

    # Проверяем понижение цены с подтверждением
    original_price = product.price
    new_price = 800.0

    with patch("builtins.input", return_value="y"):
        product.price = new_price
        assert product.price == new_price, "Цена не была понижена при подтверждении"

    # Проверяем отмену понижения цены
    original_price = product.price
    new_price = 700.0

    with patch("builtins.input", return_value="n"):
        product.price = new_price
        assert product.price == original_price, "Цена была понижена несмотря на отмену"


def test_str():
    product = Product("Смартфон", "Современный смартфон", 1000.0, 5)
    expected_str = "Смартфон, 1000.0 руб. Остаток: 5"
    assert str(product) == expected_str


def test_add():
    product1 = Product("Смартфон", "Современный смартфон", 1000.0, 5)
    product2 = Product("Ноутбук", "Мощный ноутбук", 5000.0, 2)
    total_price = product1 + product2
    expected_total_price = 1000.0 * 5 + 5000.0 * 2
    assert total_price == expected_total_price


def test_smartphone():
    # Создаём экземпляр класса Smartphone
    smartphone = Smartphone(
        "Iphone 14",
        "Смартфон с улучшенными характеристиками",
        1000.0,
        5,
        8.5,
        "14 Pro Max",
        256,
        "Black",
    )

    # Проверяем атрибуты
    assert smartphone.name == "Iphone 14"
    assert smartphone.description == "Смартфон с улучшенными характеристиками"
    assert smartphone.price == 1000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 8.5
    assert smartphone.model == "14 Pro Max"
    assert smartphone.memory == 256
    assert smartphone.color == "Black"


def test_lawn_grass():
    # Создаём экземпляр класса LawnGrass
    lawn_grass = LawnGrass(
        "Трава для газона",
        "Высококачественная трава для газона",
        50.0,
        10,
        "Россия",
        30,
        "Зеленый",
    )

    # Проверяем атрибуты
    assert lawn_grass.name == "Трава для газона"
    assert lawn_grass.description == "Высококачественная трава для газона"
    assert lawn_grass.price == 50.0
    assert lawn_grass.quantity == 10
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == 30
    assert lawn_grass.color == "Зеленый"


def test_logging_mixin():
    original_stdout = sys.stdout
    sys.stdout = StringIO()  # Перенаправляем вывод
    # Проверяем логирование при создании объекта Product
    product = Product("Продукт1", "Описание", 100.0, 10)

    captured_output = sys.stdout.getvalue()
    assert (
        "Создан объект класса 'Продукт1', описание: 'Описание', цена: 100.0, кол-во 10\n"
        == captured_output
    )
    sys.stdout = original_stdout


def test_base_product_abstract_methods():
    try:
        # Попытка создать экземпляр абстрактного класса должна вызвать ошибку
        BaseProduct("Название", "Описание", 100.0, 10)
    except TypeError as e:
        assert (
            "Can't instantiate abstract class BaseProduct without an implementation for "
            "abstract methods '__add__', '__init__', '__str__', 'new_product', 'price'"
            in str(e)
        )


def test_base_product_interface():
    # Проверяем, что все абстрактные методы присутствуют в Product
    product = Product("Продукт", "Описание", 100.0, 10)

    # Проверяем реализацию __str__
    assert str(product) == "Продукт, 100.0 руб. Остаток: 10"

    # Проверяем реализацию price getter
    assert product.price == 100.0

    # Проверяем реализацию price setter
    product.price = 150.0
    assert product.price == 150.0

    # Проверяем реализацию new_product
    new_product_data = {
        "name": "Новый продукт",
        "description": "Новое описание",
        "price": 200.0,
        "quantity": 5,
    }
    new_product = Product.new_product(new_product_data)
    assert new_product.name == "Новый продукт"
    assert new_product.price == 200.0
    assert new_product.quantity == 5

    # Проверяем реализацию __add__
    another_product = Product("Другой продукт", "Описание", 150.0, 3)
    assert product + another_product == 1950.0


def test_logging_mixin_inheritance():
    original_stdout = sys.stdout
    sys.stdout = StringIO()
    # Проверяем, что миксин работает и с наследниками Product
    smartphone = Smartphone(
        "Iphone 14",
        "Смартфон с улучшенными характеристиками",
        1000.0,
        5,
        8.5,
        "14 Pro Max",
        256,
        "Black",
    )
    assert (
        "Создан объект класса 'Iphone 14', описание: 'Смартфон с улучшенными характеристиками', цена: 1000.0, кол-во 5\n"
    ) in sys.stdout.getvalue()
    lawn_grass = LawnGrass(
        "Трава для газона",
        "Высококачественная трава для газона",
        50.0,
        10,
        "Россия",
        30,
        "Зеленый",
    )
    # test_data = sys.stdout.getvalue()
    assert (
        "Создан объект класса 'Трава для газона', описание: 'Высококачественная трава для газона', цена: 50.0, кол-во 10"
        in sys.stdout.getvalue()
    )
    sys.stdout = original_stdout


def test_logging_mixin_multiple_inheritance():
    original_stdout = sys.stdout
    sys.stdout = StringIO()

    # Проверяем работу миксина при множественном наследовании
    class TestProduct(Product, LoggingMixin):
        def __init__(self, *args, **kwargs):
            # super().__init__(*args, **kwargs)
            Product.__init__(self, *args, **kwargs)
            LoggingMixin.__init__(self, *args, **kwargs)

    test_product = TestProduct("Тестовый продукт", "Описание", 200.0, 15)
    test_message = sys.stdout.getvalue()
    assert (
        "Создан объект класса 'Тестовый продукт', описание: 'Описание', цена: 200.0, кол-во 15\n"
        in test_message
    )
    sys.stdout = original_stdout
