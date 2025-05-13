from src.catalog import *

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
    assert len(category.products) == 2
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
    assert len(category.products) == 0
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
