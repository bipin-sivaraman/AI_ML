#!/usr/bin/env python3

import math

class ItemToPurchase:
    def __init__(self, name="none", price=0, qty=0):
        self.item_name = name
        # Rounding to the nearest integer, as the output shown in the requirement
        # does not have decimals.
        self.item_price = math.floor(price)
        self.item_qty = qty

    def print_item_cost(self):
        """
        Prints the cost of the items purchased.
        """

        item_cost = self.item_price * self.item_qty
        print(f"{self.item_name} {self.item_qty} @ ${self.item_price} = ${item_cost}")

if __name__ == "__main__":
    # Initialize an empty shopping cart (list of dictionaries)
    cart_items = []

    # Prompt the user for first item details
    name1 = input("\nEnter the item name: ")
    price1 = float(input("Enter the item price: "))
    qty1 = int(input("Enter the item quantity: "))

    # Create first ItemToPurchase object andd add to shopping cart
    item1 = ItemToPurchase(name1, price1, qty1)
    cart_items.append({'name' : item1.item_name, 'price': item1.item_price, 
                       'quantity': item1.item_qty})

    # Create second ItemToPurchase object andd add to shopping cart
    name2 = input("\nEnter the item name: ")
    price2 = float(input("Enter the item price: "))
    qty2 = int(input("Enter the item quantity: "))

    # Create ItemToPurchase object
    item2 = ItemToPurchase(name2, price2, qty2)
    cart_items.append({'name' : item2.item_name, 'price': item2.item_price, 
                       'quantity': item2.item_qty})

    total = 0

    print("\nTOTAL COST")
    print("-"*55)
    item1.print_item_cost()
    item2.print_item_cost()
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    print("="*55)
    print(f"Total: ${total}")
    print("-"*55)

