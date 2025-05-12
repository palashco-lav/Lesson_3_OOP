import pytest

from src.product_catalog import *

def test_product_init():
    # Создаем тестовый продукт
    product = Product(
        name="iPhone 14",
        description="Смартфон Apple",
        price=79990.0,
        quantity=10
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
        name="iPhone 14",
        description="Смартфон Apple",
        price=79990.0,
        quantity=10
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

# =====

def test_category_init():
    # Создаем тестовые продукты
    product1 = Product("iPhone 14", "Смартфон Apple", 79990.0, 10)
    product2 = Product("Samsung S22", "Смартфон Samsung", 69990.0, 15)

    # Создаем категорию с продуктами
    category = Category(
        name="Смартфоны",
        description="Категория смартфонов",
        products=[product1, product2]
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
        name="Планшеты",
        description="Категория планшетов",
        products=None
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
        products=[product1, product2, product3]
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


