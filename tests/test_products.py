
from src.products import Product, Category


def test_product_initialization():
    product = Product("Laptop", "A high-end gaming laptop.", 1500.0, 5)
    assert product.name == "Laptop"
    assert product.description == "A high-end gaming laptop."
    assert product.price == 1500.0
    assert product.quantity == 5

def test_category_initialization():
    category = Category("Electronics", "Devices and gadgets.")
    assert category.name == "Electronics"
    assert category.description == "Devices and gadgets."
    assert category.products == []
    assert Category.category_count == 1

def test_add_product_to_category():
    category = Category("Electronics", "Devices and gadgets.")
    product1 = Product("Laptop", "A high-end gaming laptop.", 1500.0, 5)
    product2 = Product("Smartphone", "Latest model smartphone.", 800.0, 10)

    category.add_product(product1)
    category.add_product(product2)

    assert category.get_product_count() == 2
    assert Category.product_count == 2

if __name__ == "__main__":
    def run_tests():
        test_product_initialization()
        test_category_initialization()
        test_add_product_to_category()
        print("Все тесты пройдены успешно!")