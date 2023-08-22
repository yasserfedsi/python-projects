class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_product(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")

    @classmethod
    def add_product(cls, products):
        product_id = len(products) + 1
        name = input("Enter the name of the new product: ")
        price = float(input("Enter the price of the new product: "))
        new_product = cls(product_id, name, price)
        products.append(new_product)
        print(f"Product '{name}' has been added.")


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"Added '{product.name}' to the cart.")

    def display_cart(self):
        print("Shopping Cart:")
        total_price = 0
        for product in self.cart:
            product.display_product()
            total_price += product.price
        print(f"Total Price: ${total_price:.2f}")


def add_product_to_cart(products, cart):
    print("Available Products:")
    for product in products:
        product.display_product()
    product_id = int(input("Enter the Product ID to add to the cart: "))
    selected_product = next((product for product in products if product.product_id == product_id), None)
    if selected_product:
        cart.add_to_cart(selected_product)
    else:
        print("Invalid Product ID.")


def main():
    products = [
        Product(1, "Shirt", 25.99),
        Product(2, "Jeans", 39.99),
        Product(3, "Shoes", 59.99)
    ]

    cart = ShoppingCart()

    while True:
        print("===========Welcome to the Online Shop===========")
        print("Commands:")
        print("1. Display available products")
        print("2. Add a product to the cart")
        print("3. Display shopping cart")
        print("4. Add a new product")
        print("5. Exit")

        command = input("Enter a command: ")

        if command == "1":
            print("Available Products:")
            for product in products:
                product.display_product()
        elif command == "2":
            add_product_to_cart(products, cart)
        elif command == "3":
            cart.display_cart()
        elif command == "4":
            Product.add_product(products)
        elif command == "5":
            print("Thank you for shopping with us! Goodbye.")
            break
        else:
            print("Invalid command. Please enter a valid command.")


if __name__ == "__main__":
    main()
