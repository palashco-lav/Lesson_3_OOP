from io import StringIO
from unittest.mock import patch

from src.category import Category, CategoryIterator
from src.product import Product


def test_category_init():
    # Создаем тестовые продукты
    product1 = Product("iPhone 14", "Смартфон Apple", 79990.0, 10)
    product2 = Product("Samsung S22", "Смартфон Samsung", 69990.0, 15)

    # Создаем категорию с продуктами
    category = Category(
        name="Смартфоны",
        description="Категория смартфонов",
        products=[product1, product2],
    )

    # Проверяем инициализацию
    assert category.name == "Смартфоны"
    assert category.description == "Категория смартфонов"
    assert category.category_product_count == 2
    assert Category.total_categories == 1
    assert Category.total_products == 2


def test_category_without_products():
    # Создаем категорию без продуктов
    category = Category(
        name="Планшеты", description="Категория планшетов", products=None
    )

    # Проверяем инициализацию
    assert category.name == "Планшеты"
    assert category.description == "Категория планшетов"
    assert category.category_product_count == 0
    assert Category.total_categories == 2
    assert Category.total_products == 2  # не изменилось, так как нет продуктов


def test_category_count():
    # Создаем несколько категорий
    category1 = Category("Ноутбуки", "Категория ноутбуков", [])
    category2 = Category("Планшеты", "Категория планшетов", [])
    category3 = Category("Смартфоны", "Категория смартфонов", [])

    # Проверяем счетчик категорий
    assert Category.total_categories == 5  # +3 новых категории
    assert category1.category_count == 5
    assert category2.category_count == 5
    assert category3.category_count == 5


def test_product_count():
    # Создаем категорию с продуктами
    product1 = Product("iPhone 14", "Смартфон Apple", 79990.0, 10)
    product2 = Product("Samsung S22", "Смартфон Samsung", 69990.0, 15)
    product3 = Product("Xiaomi 13", "Смартфон Xiaomi", 49990.0, 20)

    category = Category(
        name="Смартфоны",
        description="Категория смартфонов",
        products=[product1, product2, product3],
    )

    # Проверяем счетчик продуктов
    assert Category.total_products == 5  # +3 новых продукта в category
    assert category.product_count == 5


def test_invalid_init():
    # Проверяем валидацию входных данных
    try:
        Category(123, "Описание", [])  # некорректное имя
        assert False, "Должна быть ошибка при неверном типе имени"
    except ValueError:
        pass

    try:
        Category("", "Описание", [])  # пустое имя
        assert False, "Должна быть ошибка при пустом имени"
    except ValueError:
        pass

    try:
        Category("Категория", 123, [])  # некорректное описание
        assert False, "Должна быть ошибка при неверном типе описания"
    except ValueError:
        pass

    try:
        Category("Категория", "", [])  # пустое описание
        assert False, "Должна быть ошибка при пустом описании"
    except ValueError:
        pass

    try:
        Category("Категория", "Описание", "не список")  # некорректный тип продуктов
        assert False, "Должна быть ошибка при неверном типе списка продуктов"
    except ValueError:
        pass


def test_add_product():
    # Создаём категорию
    category = Category("Электроника", "Электронные устройства", [])

    # Создаём продукт
    product = Product("Смартфон", "Современный смартфон с большим экраном", 1000.0, 10)

    # Добавляем продукт в категорию
    category.add_product(product)

    # Проверяем, что продукт добавлен в список продуктов категории
    assert product in category._Category__products

    # Проверяем, что общее количество продуктов увеличилось
    assert category.total_products == 6


def test_get_product_info():
    # Создаём несколько продуктов
    product1 = Product("Смартфон", "Современный смартфон с большим экраном", 1000.0, 10)
    product2 = Product("Ноутбук", "Мощный ноутбук для работы", 5000.0, 5)

    # Создаём категорию и добавляем продукты
    category = Category("Электроника", "Электронные устройства", [product1, product2])

    # Проверяем вывод информации о продуктах
    expected_output = (
        "Смартфон, 1000.0 руб. Остаток: 10 шт.\n" "Ноутбук, 5000.0 руб. Остаток: 5 шт."
    )
    with patch("sys.stdout", new=StringIO()) as fake_out:
        print(category.get_product_info)
        assert fake_out.getvalue().strip() == expected_output.strip()


def test_str():
    # Создаём несколько продуктов
    product1 = Product("Смартфон", "Современный смартфон с большим экраном", 1000.0, 10)
    product2 = Product("Ноутбук", "Мощный ноутбук для работы", 5000.0, 5)

    # Создаём категорию и добавляем продукты
    category = Category("Электроника", "Электронные устройства", [product1, product2])

    # Проверяем вывод информации о категории
    expected_str = "Электроника, количество продуктов: 15"
    assert str(category) == expected_str


def test_category_iterator():
    # Создаём несколько продуктов
    product1 = Product("Смартфон", "Современный смартфон с большим экраном", 1000.0, 10)
    product2 = Product("Ноутбук", "Мощный ноутбук для работы", 5000.0, 5)

    # Создаём категорию и добавляем продукты
    category = Category("Электроника", "Электронные устройства", [product1, product2])

    # Создаём итератор для категории
    category_iterator = CategoryIterator(category)

    # Проверяем итерацию по товарам
    products = []
    for product in category_iterator:
        products.append(product)

    assert products == [product1, product2]


def test_products_property():
    # Создаём несколько продуктов
    product1 = Product("Смартфон", "Современный смартфон с большим экраном", 1000.0, 10)
    product2 = Product("Ноутбук", "Мощный ноутбук для работы", 5000.0, 5)

    # Создаём категорию и добавляем продукты
    category = Category("Электроника", "Электронные устройства", [product1, product2])

    # Проверяем свойство products
    expected_products_info = f"{product1}\n" f"{product2}\n"
    assert category.products == expected_products_info
