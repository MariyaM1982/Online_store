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
        if existing_products is None:
            existing_products = []

        product_name = product_info.get("name")
        product_description = product_info.get("description")
        product_price = product_info.get("price")
        product_quantity = product_info.get("quantity")

        for existing_product in existing_products:
            if existing_product.name == product_name:
                existing_product.quantity += product_quantity
                existing_product.price = max(existing_product.price, product_price)
                return existing_product

        return cls(product_name, product_description, product_price, product_quantity)

    def __str__(self):
        """Возвращает строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Возвращает общую стоимость двух продуктов."""
        if isinstance(other, Product):
            total_value_self = self.price * self.quantity
            total_value_other = other.price * other.quantity
            return total_value_self + total_value_other
        return NotImplemented  # Возвращаем NotImplemented, если операция невозможна


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, l):
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут для хранения списка продуктов
        Category.category_count += 1

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError("Только объекты класса Product могут быть добавлены.")

    @property
    def products(self):
        """Геттер для получения списка продуктов в формате строки."""
        if not self.__products:
            return "Нет продуктов в категории."

        return "\n".join(str(product) for product in self.__products)

    def __iter__(self):
        """Возвращает итератор для перебора продуктов в категории."""
        return ProductIterator(self)

    @classmethod
    def get_product_count(cls):
        return cls.product_count

    @classmethod
    def get_category_count(cls):
        return cls.category_count

    def __str__(self):
        """Возвращает строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class ProductIterator:
    def __init__(self, category):
        self.category = category
        self.index = 0  # Начальный индекс для итерации

    def __iter__(self):
        """Возвращает сам итератор."""
        return self

    def __next__(self):
        """Возвращает следующий продукт в категории."""
        if self.index < len(self.category._Category__products):
            product = self.category._Category__products[self.index]
            self.index += 1
            return product
        raise StopIteration  # Завершение итерации
