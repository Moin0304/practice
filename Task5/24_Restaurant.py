# 24.Write a Python class Restaurant with attributes like menu_items, book_table, and
#  customer_orders, and methods like add_item_to_menu, book_tables, and customer_order. 
# Perform the following tasks now:
# -Now add items to the menu.
# -Make table reservations.
# -Take customer orders.
# -Print the menu.
# -Print table reservations.
# -Print customer orders.

# Note : Use dictionaries and lists to store the data.

class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.booked_tables = []
        self.customer_orders = []

    def add_item_to_menu(self, item_name, item_price):
        self.menu_items[item_name] = item_price

    def book_table(self, table_number):
        self.booked_tables.append(table_number)

    def customer_order(self, table_number, order_items):
        self.customer_orders.append({'table_number': table_number, 'order_items': order_items})

    def print_menu(self):
        print('Menu:')
        for item_name, item_price in self.menu_items.items():
            print(f'{item_name}: RS. {item_price}')

    def print_booked_tables(self):
        print('Booked Tables:')
        print(self.booked_tables)

    def print_customer_orders(self):
        print('Customer Orders:')
        for order in self.customer_orders:
            print(f'Table {order["table_number"]}: {", ".join(order["order_items"])}')

restaurant = Restaurant()

restaurant.add_item_to_menu('Burger', 60)
restaurant.add_item_to_menu('Pizza', 100)
restaurant.add_item_to_menu('Fries', 70)

restaurant.book_table(1)
restaurant.book_table(2)
restaurant.book_table(3)

restaurant.customer_order(1, ['Burger', 'Fries'])
restaurant.customer_order(2, ['Pizza', 'Fries'])
restaurant.customer_order(3, ['Burger', 'Pizza', 'Fries'])

restaurant.print_menu()
restaurant.print_booked_tables()
restaurant.print_customer_orders()
