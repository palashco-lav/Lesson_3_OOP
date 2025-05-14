from unittest.mock import patch

from src.product import Product


def test_product_init():
    # Создаем тестовый продукт
    product = Product(
        name="iPhone 14", description="Смартфон Apple", price=79990.0, quantity=10
    )

    # Проверяем корректность инициализации
    assert product.name == "iPhone 14"
    assert product.description == "Смартфон Apple"
    assert product.price == 79990.0
    assert product.quantity == 10


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
