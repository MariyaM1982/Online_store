import unittest

from src.products import Category, Product


def test_product_initialization():
    product = Product("Laptop", "A high-end gaming laptop.", 1500.0, 5)
    assert product.name == "Laptop"
    assert product.description == "A high-end gaming laptop."
    assert product.price == 1500.0
    assert product.quantity == 5


def test_category_initialization():
    product1 = Product("Laptop", "A high-end gaming laptop.", 1500.0, 5)
    product2 = Product("Smartphone", "Latest model smartphone.", 800.0, 10)
    product3 = Product("PlayStation", "Latest model PlayStation.", 2000.0, 15)
    category = Category(
        "Electronics", "Devices and gadgets.", [product1, product2, product3]
    )
    assert category.name == "Electronics"
    assert category.description == "Devices and gadgets."
    assert Category.category_count == 1


def test_add_product_to_category():
    product1 = Product("Laptop", "A high-end gaming laptop.", 1500.0, 5)
    product2 = Product("Smartphone", "Latest model smartphone.", 800.0, 10)
    product3 = Product("PlayStation", "Latest model PlayStation.", 2000.0, 15)
    category = Category(
        "Electronics", "Devices and gadgets.", [product1, product2, product3]
    )

    category.add_product(product1)
    category.add_product(product2)

    assert category.get_product_count() == 2
    assert Category.product_count == 2


class TestProductCategory(unittest.TestCase):
    def setUp(self):
        """Подготовка данных для тестов."""
        self.category = Category("Электроника", "Категория для электроники", [])
        self.product1 = Product("Телевизор", "4K LED экран", 30000, 15)
        self.product2 = Product("Смартфон", "Android смартфон", 20000, 10)
        self.product3 = Product("Ноутбук", "Игровой ноутбук", 70000, 5)
        self.product1_info = {
            "name": "Яблоко",
            "description": "Сочное яблоко",
            "price": 50,
            "quantity": 10,
        }
        self.product2_info = {
            "name": "Апельсин",
            "description": "Сладкий апельсин",
            "price": 70,
            "quantity": 5,
        }
        self.existing_products = []  # Список для хранения существующих продуктов
        self.category = Category(
            "Фрукты",
            "Разнообразные фрукты",
            [self.product1, self.product2, self.product3],
        )

    def test_new_product_creation(self):
        """Тест на создание нового продукта."""
        product1 = Product.new_product(self.product1_info, self.existing_products)
        self.existing_products.append(product1)

        self.assertEqual(product1.name, "Яблоко")
        self.assertEqual(product1.price, 50)
        self.assertEqual(product1.quantity, 10)

    def test_product_update_existing(self):
        """Тест на обновление существующего продукта."""
        product1 = Product.new_product(self.product1_info, self.existing_products)
        self.existing_products.append(product1)

        product_update_info = {
            "name": "Яблоко",
            "description": "Сочное яблоко (обновленный)",
            "price": 60,  # Максимальная цена должна быть 60
            "quantity": 5,  # Обновляем количество
        }

        updated_product = Product.new_product(
            product_update_info, self.existing_products
        )

        self.assertEqual(
            updated_product.quantity, 15
        )  # Проверка обновленного количества
        self.assertEqual(updated_product.price, 60)  # Проверка обновленной цены

    def test_add_product_to_category(self):
        """Тест на добавление продукта в категорию."""
        product1 = Product.new_product(self.product1_info, self.existing_products)
        self.category.add_product(product1)

        self.assertIn(
            product1, self.category._Category__products
        )  # Проверка добавления продукта
        self.assertEqual(
            Category.get_product_count(), 1
        )  # Проверка общего количества продуктов

    def test_get_category_products(self):
        """Тест на получение списка продуктов из категории."""
        product1 = Product.new_product(self.product1_info, self.existing_products)
        product2 = Product.new_product(self.product2_info, self.existing_products)
        self.category.add_product(product1)
        self.category.add_product(product2)

        expected_output = (
            "Яблоко, 50 руб. Остаток: 10 шт.\n" "Апельсин, 70 руб. Остаток: 5 шт."
        )
        self.assertEqual(self.category.products.strip(), expected_output)

    def test_no_products_in_category(self):
        """Тест на случай, когда в категории нет продуктов."""
        self.assertEqual(self.category.products.strip(), "Нет продуктов в категории.")

    def tearDown(self):
        """Очистка данных после тестов. Обязательно если тесты выполняются в рамках одного выполнения."""
        Category.category_count = 0
        Category.product_count = 0
        self.existing_products.clear()
        self.category._Category__products.clear()


class TestProductAndCategory(unittest.TestCase):

    def setUp(self):
        """Настройка необходимых объектов для тестов."""
        self.category = Category("Электроника", "Категория для электроники", [])
        self.product1 = Product("Телевизор", "4K LED экран", 30000, 15)
        self.product2 = Product("Смартфон", "Android смартфон", 20000, 10)
        self.product3 = Product("Ноутбук", "Игровой ноутбук", 70000, 5)

    def test_add_product(self):
        """Тест для добавления продукта в категорию и проверки количества продуктов."""
        self.category.add_product(self.product1)
        self.assertIn(self.product1, self.category._Category__products)
        self.assertEqual(Category.get_product_count(), 1)

    def test_add_multiple_products(self):
        """Тест для добавления нескольких продуктов и проверки количества."""
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)
        self.assertEqual(Category.get_product_count(), 2)
        self.assertIn(self.product1, self.category._Category__products)
        self.assertIn(self.product2, self.category._Category__products)

    def test_product_initialization(self):
        """Тест для проверки корректной инициализации продукта."""
        self.assertEqual(self.product1.name, "Телевизор")
        self.assertEqual(self.product1.description, "4K LED экран")
        self.assertEqual(self.product1.price, 30000)
        self.assertEqual(self.product1.quantity, 15)

    def test_product_update_quantity_and_price(self):
        """Тест для проверки обновления количества и цены продукта."""
        product_info = {
            "name": "Телевизор",
            "description": "4K LED экран",
            "price": 35000,
            "quantity": 5,
        }

        new_product = Product.new_product(product_info, [self.product1])
        self.assertEqual(new_product.quantity, 20)  # 15 + 5
        self.assertEqual(new_product.price, 35000)  # Максимальная цена

    def test_product_addition_with_different_name(self):
        """Тест для проверки добавления нового продукта с другим именем."""
        product_info = {
            "name": "Микроволновка",
            "description": "СВЧ печь",
            "price": 8000,
            "quantity": 3,
        }

        new_product = Product.new_product(product_info, [self.product1])
        self.assertEqual(new_product.name, "Микроволновка")
        self.assertEqual(new_product.price, 8000)
        self.assertEqual(new_product.quantity, 3)

    def test_iterator(self):
        """Тест для проверки корректности работы итератора."""
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)

        products = [product for product in self.category]

        self.assertEqual(len(products), 2)
        self.assertIn(self.product1, products)
        self.assertIn(self.product2, products)

    def test_get_category_count(self):
        """Тест для проверки общего количества категорий."""
        self.assertEqual(Category.get_category_count(), 1)

    def test_category_string_representation(self):
        """Тест для проверки строкового представления категории."""
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)
        self.assertEqual(
            str(self.category), "Электроника, количество продуктов: 25 шт."
        )


if __name__ == "__main__":

    def run_tests():
        test_product_initialization()
        test_category_initialization()
        test_add_product_to_category()
        print("Все тесты пройдены успешно!")
