class Restaurant:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return f"{self.name} - Address: {self.address}, Phone: {self.phone}"


class MenuItem:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name} - ${self.price}\nDescription: {self.description}"


class Menu:
    def __init__(self):
        self.menu_items = []

    def add_item(self, item):
        self.menu_items.append(item)

    def remove_item(self, item):
        self.menu_items.remove(item)

    def __str__(self):
        menu_str = "Menu:\n"
        for item in self.menu_items:
            menu_str += f"{item}\n"
        return menu_str


class Customer:
    def __init__(self, name):
        self.name = name
        self.order = []

    def add_to_order(self, item):
        self.order.append(item)

    def remove_from_order(self, item):
        self.order.remove(item)

    def view_order(self):
        if not self.order:
            return "Your order is empty."
        order_str = "Your order:\n"
        for item in self.order:
            order_str += f"{item}\n"
        return order_str

    def pay_bill(self):
        total_cost = sum(item.price for item in self.order)
        return total_cost


def main():
    # Create a Restaurant
    restaurant = Restaurant("Tasty Bites", "123 Main St, Cityville", "555-1234")

    # Create Menu Items
    item1 = MenuItem("Spaghetti Bolognese", 12.99, "Classic Italian pasta dish.")
    item2 = MenuItem("Chicken Alfredo", 14.99, "Creamy pasta with grilled chicken.")
    item3 = MenuItem("Cheesecake", 6.99, "Delicious homemade cheesecake.")

    # Create a Menu
    menu = Menu()
    menu.add_item(item1)
    menu.add_item(item2)
    menu.add_item(item3)

    # Create a Customer
    customer = Customer("John")

    while True:
        print("\nWelcome to", restaurant.name)
        print("1. View Menu")
        print("2. Order Food")
        print("3. View Order")
        print("4. Pay Bill")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            print("\nMenu:")
            print(menu)

        elif choice == "2":
            print("\nMenu:")
            print(menu)
            item_number = int(input("Enter the item number you want to order: ")) - 1
            if 0 <= item_number < len(menu.menu_items):
                customer.add_to_order(menu.menu_items[item_number])
                print("Item added to your order.")
            else:
                print("Invalid item number. Please try again.")

        elif choice == "3":
            print(customer.view_order())

        elif choice == "4":
            total_cost = customer.pay_bill()
            print(f"Your total bill amount is ${total_cost:.2f}")
            payment = input("Enter your payment method (cash/card): ")
            if payment.lower() == "cash":
                amount_paid = float(input("Enter the amount you are paying: "))
                if amount_paid >= total_cost:
                    change = amount_paid - total_cost
                    print(f"Thank you! Your change is ${change:.2f}")
                    break
                else:
                    print("Insufficient amount. Please try again.")
            elif payment.lower() == "card":
                print("Payment successful. Thank you!")
                break
            else:
                print("Invalid payment method. Please try again.")

        elif choice == "5":
            print("Thank you for visiting. Have a great day!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

    
