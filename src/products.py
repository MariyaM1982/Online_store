class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = None  # Приватный атрибут для хранения цены
        self.price = price  # Используем сеттер для установки начальной цены
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для получения цены товара."""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для установки цены товара с проверкой."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value  # Установка новой цены, если она положительная

    @classmethod
    def new_product(cls, product_info, existing_products=None):
        """
        Создает новый продукт или обновляет существующий, если уже есть продукт с таким именем.

        :param product_info: Словарь с параметрами товара (name, description, price, quantity).
        :param existing_products: Список существующих продуктов для проверки дубликатов.
        :return: Экземпляр класса Product.
        """
        if existing_products is None:
            existing_products = []

        product_name = product_info.get("name")
        product_description = product_info.get("description")
        product_price = product_info.get("price")
        product_quantity = product_info.get("quantity")

        # Проверка на существование товара с таким же именем
        for existing_product in existing_products:
            if existing_product.name == product_name:
                # Обновляем количество и выбираем максимальную цену
                existing_product.quantity += product_quantity
                existing_product.price = max(existing_product.price, product_price)
                return existing_product  # Возвращаем обновленный продукт

        # Если товара с таким именем не существует, создаем новый
        return cls(product_name, product_description, product_price, product_quantity)


class Category:
    category_count = 0  # Общий счетчик категорий
    product_count = 0  # Общий счетчик продуктов

    def __init__(self, name, description, l):
        # self._Category__products = None
        self._Category__products = None
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут для хранения списка продуктов
        Category.category_count += 1  # Увеличиваем счетчик категорий

    def add_product(self, product):
        if isinstance(product, Product):  # Проверка типа продукта
            self.__products.append(product)  # Добавляет продукт в список
            Category.product_count += 1  # Увеличиваем счетчик продуктов
        else:
            raise ValueError("Только объекты класса Product могут быть добавлены.")

    @property
    def products(self):
        """Геттер для получения списка продуктов в формате строки."""
        if not self.__products:  # Проверяем, пустой ли список
            return "Нет продуктов в категории."

        products_list = []
        for product in self.__products:
            product_info = (
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            )
            products_list.append(product_info)

        return "\n".join(products_list)  # Возвращаем продукты в формате строки

    @classmethod
    def get_product_count(cls):
        return cls.product_count  # Метод для получения общего количества продуктов

    @classmethod
    def get_category_count(cls):
        return cls.category_count  # Метод для получения общего количества категорий
