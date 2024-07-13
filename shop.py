class Item:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def value_sum(self):
        return self.price * self.count


class Shop:
    def __init__(self):
        self.products = []

    def print_inventory(self):
        print("   Nazwa   | Ilość | Cena | Wartość ")
        print("-----------|-------|------|---------")
        for product in self.products:
            print(
                f"{product.name:>10s} |{product.count:6d} |"
                f"{product.price:^6.2f}|{product.value_sum():8.2f}"
            )

    def buy_product(self, product_name, count):
        product = next(
            product for product in self.products if product.name == product_name
        )
        if product.count >= count:
            produkt.count -= count


shop = Shop()
shop.products = [
    Item("marchewka", 2.99, 400),
    Item("chleb", 5.80, 50),
    Item("woda", 3.0, 20),
]
shop.print_inventory()
