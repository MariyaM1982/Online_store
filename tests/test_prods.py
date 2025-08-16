import unittest

from src.products import (
    BaseEntity,
    BaseProduct,
    Category,
    CreationInfoMixin,
    LawnGrass,
    Order,
    Product,
    ProductIterator,
    Smartphone,
)


class TestStore(unittest.TestCase):

    def setUp(self):
        """Настройка необходимых объектов для тестов."""
        self.smartphone = Smartphone(
            "iPhone 13",
            "Смартфон от Apple",
            80000,
            5,
            "A15 Bionic",
            "iPhone 13",
            128,
            "Черный",
        )
        self.grass = LawnGrass(
            "Газонная трава",
            "Смешанная трава для газонов",
            1500,
            20,
            "Россия",
            14,
            "Зеленый",
        )
        self.existing_products = [self.smartphone]

    def test_product_creation(self):
        """Тест для проверки создания продукта."""
        self.assertIsInstance(self.smartphone, Product)
        self.assertEqual(self.smartphone.name, "iPhone 13")

    def test_product_string(self):
        """Тест для проверки корректного отображения строки продукта."""
        self.assertEqual(
            str(self.smartphone),
            "Продукт: iPhone 13, Описание: Смартфон от Apple, Цена: 80000, Количество: 5",
        )

    def test_product_price_setter(self):
        """Тест для проверки установщика цены."""
        self.smartphone.price = 75000
        self.assertEqual(self.smartphone.price, 75000)

    def test_product_price_setter_negative(self):
        """Тест для проверки установщика цены с отрицательным значением."""
        self.smartphone.price = -100
        self.assertEqual(self.smartphone.price, 75000)  # Не должно измениться

    def test_product_new_product_creates_new(self):
        """Тест для проверки метода new_product - создание нового продукта."""
        product_info = {
            "name": "Samsung Galaxy S21",
            "description": "Смартфон от Samsung",
            "price": 70000,
            "quantity": 10,
        }
        new_product = Product.new_product(product_info, self.existing_products)
        self.assertIsInstance(new_product, Smartphone)
        self.assertEqual(new_product.name, "Samsung Galaxy S21")

    def test_product_new_product_updates_existing(self):
        """Тест для проверки метода new_product - обновление существующего продукта."""
        product_info = {
            "name": "iPhone 13",
            "description": "Смартфон от Apple",
            "price": 80000,
            "quantity": 3,
        }
        updated_product = Product.new_product(product_info, self.existing_products)
        self.assertEqual(updated_product.quantity, 8)  # Количество должно увеличиться
        self.assertEqual(updated_product.price, 80000)  # Цена должна остаться той же

    def test_product_addition(self):
        """Тест для проверки перегрузки оператора +."""
        total_value = self.smartphone + self.grass
        expected_value = (self.smartphone.price * self.smartphone.quantity) + (
            self.grass.price * self.grass.quantity
        )
        self.assertEqual(total_value, expected_value)

    def test_smartphone_string(self):
        """Тест для проверки строки смартфона."""
        self.smartphone.price = 80000  # Убедимся, что цена корректная
        self.assertEqual(
            str(self.smartphone),
            "Продукт: iPhone 13, Описание: Смартфон от Apple, Цена: 80000, Количество: 5",
        )

    def test_lawn_grass_string(self):
        """Тест для проверки строки газонной травы."""
        self.assertEqual(
            str(self.grass),
            "Продукт: Газонная трава, Описание: Смешанная трава для газонов, Цена: 1500, Количество: 20",
        )

    def test_lawn_grass_creation(self):
        """Тест для проверки создания газонной травы."""
        self.assertIsInstance(self.grass, LawnGrass)

    def test_lawn_grass_initial_attributes(self):
        """Тест для проверки атрибутов газонной травы."""
        self.assertEqual(self.grass.country, "Россия")
        self.assertEqual(self.grass.germination_period, 14)
        self.assertEqual(self.grass.color, "Зеленый")

        class TestOrder(unittest.TestCase):
            def setUp(self):
                self.product = Product("iPhone 13", "Смартфон от Apple", 80000, 5)
                self.order = Order(self.product, 3)

            def test_order_creation(self):
                self.assertEqual(self.order.product, self.product)
                self.assertEqual(self.order.quantity, 3)
                self.assertEqual(self.order.total_cost, 240000)

            def test_order_string(self):
                self.assertEqual(
                    str(self.order),
                    "Заказ: iPhone 13, Количество: 3, Итоговая стоимость: 240000 руб.",
                )

            def test_order_invalid_product(self):
                with self.assertRaises(TypeError):
                    Order("непродукт", 3)


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.product = Product("iPhone 13", "Смартфон от Apple", 80000, 5)
        self.order = Order(self.product, 3)

    def test_order_creation(self):
        self.assertEqual(self.order.product, self.product)
        self.assertEqual(self.order.quantity, 3)
        self.assertEqual(self.order.total_cost, 240000)

    def test_order_string(self):
        self.assertEqual(
            str(self.order),
            "Заказ: iPhone 13, Количество: 3, Итоговая стоимость: 240000 руб.",
        )

    def test_order_invalid_product(self):
        with self.assertRaises(TypeError):
            Order("непродукт", 3)


class TestCategory(unittest.TestCase):
    def setUp(self):
        self.category = Category("Смартфоны", "Категория для смартфонов", [])
        self.product1 = Product("iPhone 13", "Смартфон от Apple", 80000, 5)
        self.product2 = Product("Samsung Galaxy S21", "Смартфон от Samsung", 70000, 10)

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Смартфоны")
        self.assertEqual(self.category.description, "Категория для смартфонов")
        self.assertEqual(Category.get_category_count(), 1)

    def test_add_product(self):
        self.category.add_product(self.product1)
        self.assertIn(self.product1, self.category._Category__products)
        self.assertEqual(Category.get_product_count(), 1)

    def test_add_invalid_product(self):
        with self.assertRaises(TypeError):
            self.category.add_product("непродукт")

    def test_products_string(self):
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)
        self.assertIn("iPhone 13", str(self.category))
        self.assertIn("Samsung Galaxy S21", str(self.category))

    def test_products_property(self):
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)
        products_string = self.category.products
        self.assertIn("iPhone 13", products_string)
        self.assertIn("Samsung Galaxy S21", products_string)

    def test_empty_products_string(self):
        self.assertEqual(self.category.products, "Нет продуктов в категории.")


class TestProductIterator(unittest.TestCase):
    def setUp(self):
        self.category = Category("Смартфоны", "Категория для смартфонов", [])
        self.product1 = Product("iPhone 13", "Смартфон от Apple", 80000, 5)
        self.product2 = Product("Samsung Galaxy S21", "Смартфон от Samsung", 70000, 10)
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)

    def test_iterator(self):
        products = [product for product in self.category]
        self.assertEqual(products, [self.product1, self.product2])

    def test_iterator_empty(self):
        empty_category = Category("Пустая категория", "Нет продуктов", [])
        products = list(empty_category)
        self.assertEqual(products, [])


class TestProductQuantityValidation(unittest.TestCase):
    def test_zero_quantity_raises_error(self):
        """Тест проверки валидации нулевого количества товара"""
        with self.assertRaises(ValueError):
            Product("Товар", "Описание", 100, 0)

    def test_negative_quantity_raises_error(self):
        """Тест проверки валидации отрицательного количества товара"""
        with self.assertRaises(ValueError):
            Product("Товар", "Описание", 100, -5)

    def test_positive_quantity_works(self):
        """Тест проверки корректной работы с положительным количеством"""
        product = Product("Товар", "Описание", 100, 10)
        self.assertEqual(product.quantity, 10)


class TestCategoryAveragePrice(unittest.TestCase):
    def setUp(self):
        self.category = Category("Тестовая категория", "Описание категории", [])
        self.product1 = Product("Продукт 1", "Описание 1", 100, 5)
        self.product2 = Product("Продукт 2", "Описание 2", 200, 3)
        self.product3 = Product("Продукт 3", "Описание 3", 150, 2)

    def test_average_price_empty_category(self):
        """Тест проверки средней цены для пустой категории"""
        self.assertEqual(self.category.get_average_price(), 0.0)

    def test_average_price_single_product(self):
        """Тест проверки средней цены для одной позиции"""
        self.category.add_product(self.product1)
        self.assertEqual(self.category.get_average_price(), 100.0)

    def test_average_price_multiple_products(self):
        """Тест проверки средней цены для нескольких позиций"""
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)
        self.category.add_product(self.product3)

        # Расчет ожидаемого результата: (100 + 200 + 150) / 3 = 150
        self.assertEqual(self.category.get_average_price(), 150.0)

    def test_average_price_with_different_quantities(self):
        """Тест проверки средней цены с учетом разного количества"""
        # Здесь проверяем, что количество не влияет на расчет средней цены
        self.category.add_product(self.product1)  # 100
        self.category.add_product(self.product2)  # 200
        self.category.add_product(self.product3)  # 150

        # Расчет: (100 + 200 + 150) / 3 = 150
        self.assertEqual(self.category.get_average_price(), 150.0)

    def test_average_price_with_zero_division(self):
        """Тест проверки обработки деления на ноль"""
        # Категория изначально пустая
        self.assertEqual(self.category.get_average_price(), 0.0)
