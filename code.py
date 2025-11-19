class User:
    def __init__(self, user_id, name, contact, address):
        self.user_id = user_id
        self.name = name
        self.contact = contact
        self.address = address
        self.cart = Cart(self)

class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name

class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

class Cart:
    def __init__(self, user):
        self.user = user
        self.items = []  # List of Product objects

    def add_product(self, product):
        self.items.append(product)
        print(f"{product.name} added to cart")

    def view_cart(self):
        print("Cart Items:")
        for item in self.items:
            print(f"{item.name} - ₹{item.price}")

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

class Order:
    def __init__(self, order_id, user, cart_items):
        self.order_id = order_id
        self.user = user
        self.items = cart_items
        self.total = sum(item.price for item in cart_items)

    def confirm_order(self):
        print(f"Order #{self.order_id} confirmed for {self.user.name}")
        print(f"Total amount: ₹{self.total}")

# Sample usage:

indian_wear = Category(1, "Indian Wear")
western_wear = Category(2, "Western Wear")

products = [
    Product(101, "Saree", 1200, indian_wear),
    Product(102, "Kurti", 600, indian_wear),
    Product(201, "T-Shirt", 400, western_wear),
    Product(202, "Jeans", 1000, western_wear),
]

user = User(1, "Amit Kumar", "9876543210", "Delhi")

# User adds products to cart
user.cart.add_product(products[0])  # Saree
user.cart.add_product(products[3])  # Jeans

# View cart and total bill
user.cart.view_cart()
print(f"Total Bill: ₹{user.cart.calculate_total()}")

# Place order
order = Order(5001, user, user.cart.items)
order.confirm_order()
