import unittest

from src.products import Category, LawnGrass, Product, Smartphone


class TestProduct(unittest.TestCase):
    def setUp(self):
        """Создает экземпляры для использования в тестах."""
        self.product = Product("Товар 1", "Описание товара 1", 100, 50)

    def test_initialization(self):
        """Проверяет правильно ли инициализируются атрибуты товара."""
        self.assertEqual(self.product.name, "Товар 1")
        self.assertEqual(self.product.description, "Описание товара 1")
        self.assertEqual(self.product.price, 100)
        self.assertEqual(self.product.quantity, 50)

    def test_price_setter_valid(self):
        """Проверяет установку положительной цены."""
        self.product.price = 150
        self.assertEqual(self.product.price, 150)

    def test_price_setter_invalid(self):
        """Проверяет установку отрицательной цены."""
        with self.assertRaises(ValueError) as context:
            self.product.price = -50
        self.assertEqual(
            str(context.exception), "Цена не должна быть нулевая или отрицательная"
        )

    def test_str_representation(self):
        """Проверяет строковое представление товара."""
        self.assertEqual(str(self.product), "Товар 1, 100 руб. Остаток: 50 шт.")

    def test_addition(self):
        """Проверяет сложение стоимости двух товаров."""
        product2 = Product("Товар 2", "Описание товара 2", 200, 30)
        total = self.product + product2
        self.assertEqual(total, (100 * 50) + (200 * 30))


class TestSmartphone(unittest.TestCase):
    def setUp(self):
        """Создает экземпляр смартфона для тестов."""
        self.smartphone = Smartphone(
            "Смартфон 1",
            "Описание смартфона 1",
            30000,
            10,
            "Высокая",
            "Модель X",
            64,
            "Чёрный",
        )

    def test_str_representation(self):
        """Проверяет строковое представление смартфона."""
        expected_str = "Смартфон 1, 30000 руб. Остаток: 10 шт., Модель: Модель X, Эффективность: Высокая, Память: 64 ГБ, Цвет: Чёрный"
        self.assertEqual(str(self.smartphone), expected_str)


class TestLawnGrass(unittest.TestCase):
    def setUp(self):
        """Создает экземпляр газона для тестов."""
        self.lawn_grass = LawnGrass(
            "Газон 1", "Описание газона 1", 500, 20, "Россия", 10, "Зелёный"
        )

    def test_str_representation(self):
        """Проверяет строковое представление газона."""
        expected_str = "Газон 1, 500 руб. Остаток: 20 шт., Страна-производитель: Россия, Срок прорастания: 10 дн., Цвет: Зелёный"
        self.assertEqual(str(self.lawn_grass), expected_str)


class TestCategory(unittest.TestCase):
    def setUp(self):
        """Создает экземпляр категории для тестов."""
        self.category = Category("Электроника", "Описание электроники", [])
        self.product = Product("Тестовый продукт", 10.0, 10, 500)

    def test_add_product(self):
        """Проверяет добавление продукта в категорию."""
        self.category.add_product(self.category)
        self.assertEqual(Category.get_product_count(), 0)  # должно вызывать ошибку

    def test_add_invalid_product(self):
        """Проверяет, что не удастся добавить не-продукт."""
        with self.assertRaises(TypeError):
            self.category.add_product("Неправильный тип")

    def test_str_representation(self):
        """Проверяет строковое представление категории."""
        self.assertEqual(str(self.category), "Электроника, количество продуктов: 0 шт.")
