class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_product(self):
        print(f"{self.product_id}. {self.name} - ${self.price}")


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"{product.name} added to cart")

    def remove_product(self, product_id):
        for product in self.items:
            if product.product_id == product_id:
                self.items.remove(product)
                print(f"{product.name} removed from cart")
                return

        print("Product not found")

    def show_cart(self):
        if not self.items:
            print("Cart is empty")
            return

        print("\nYour Cart:")
        total = 0

        for product in self.items:
            print(f"{product.name} - ${product.price}")
            total += product.price

        print(f"Total: ${total}")

    def checkout(self):
        total = sum(product.price for product in self.items)

        print("\nCheckout Successful!")
        print(f"Total Amount: ${total}")

        self.items.clear()


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def view_products(self, products):
        print("\nAvailable Products:")
        for product in products:
            product.display_product()


# Products
products = [
    Product(1, "Laptop", 800),
    Product(2, "Phone", 500),
    Product(3, "Headphones", 100),
    Product(4, "Keyboard", 50)
]


# Customer
customer = Customer("Ali")


while True:
    print("\n===== Online Shopping System =====")
    print("1. View Products")
    print("2. Add Product")
    print("3. Remove Product")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        customer.view_products(products)

    elif choice == "2":
        product_id = int(input("Enter product id: "))

        for product in products:
            if product.product_id == product_id:
                customer.cart.add_product(product)
                break
        else:
            print("Product not found")


    elif choice == "3":
        product_id = int(input("Enter product id: "))
        customer.cart.remove_product(product_id)


    elif choice == "4":
        customer.cart.show_cart()


    elif choice == "5":
        customer.cart.checkout()


    elif choice == "6":
        print("Thank you for shopping!")
        break


    else:
        print("Invalid choice")