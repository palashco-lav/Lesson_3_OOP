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