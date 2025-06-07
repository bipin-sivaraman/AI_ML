#!/usr/bin/env python3

import math
import re

alert = '\033[91m'
reset = '\033[0m'

class DateError(Exception):
    pass

class ItemToPurchase:
    def __init__(self, name="none", price=0, qty=0):
        self.item_name = name
        # Rounding to the nearest integer, as the output shown in the requirement
        # does not have decimals.
        self.item_price = math.floor(price)
        self.item_qty = qty
        self.item_desc = None
        self.item_cost = 0

    def print_item_cost(self):
        """
        Prints the cost of the items purchased.
        """

        self.item_cost = self.item_price * self.item_qty
        print(f"{self.item_name} {self.item_qty} @ ${self.item_price:.0f} = ${self.item_cost:.0f}")

class ShoppingCart(ItemToPurchase):
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    
    def add_item(self, item_to_purchase):
        """
        Adds an item to cart_items list. 
        """

        self.cart_items.append(item_to_purchase)
    
    def remove_item(self, item_name):
        """
        Removes item from cart_items.
        """

        item_found = False
        for obj in self.cart_items:
            if obj.item_name == item_name:
                self.cart_items.remove(obj)
                item_found = True

        if not item_found:
            print(f'{alert}Item not found in cart. Nothing removed.{reset}')

    def modify_item(self, item_to_purchase):
        """
        Modifies an items description, price, and/or quantity.
        """

        item_found = False
        index = 0
        for obj in self.cart_items:
            if obj.item_name == item_to_purchase.item_name:
                if item_to_purchase.item_price != 0:
                    # Updating the item's price in cart.
                    self.cart_items[index].item_price = item_to_purchase.item_price
                if item_to_purchase.item_qty != 0:
                    # Updating the item's quantity in cart.
                    self.cart_items[index].item_qty = item_to_purchase.item_qty
                # Updating item description.
                if item_to_purchase.item_desc is not None:
                    self.cart_items[index].item_desc = item_to_purchase.item_desc
                item_found = True
                break
            index += 1

        if not item_found:
            print(f'{alert}Item not found in cart. Nothing modified.{reset}')

    def __get_num_items_in_cart(self):
        """
        Returns quantity of all items in cart.
        """

        item_count = 0
        for item in self.cart_items:
            item_count +=  item.item_qty 
        return item_count

    def __get_cost_of_cart(self):
        """
        Determines and returns the total cost of items in cart.
        """
        
        total = 0
        for item in self.cart_items:
            item.print_item_cost()
            total += item.item_cost
        
        return total

    def print_total(self):
        """
        Outputs total of objects in cart.
        """

        print(f"{self.customer_name}'s Shopping Cart - {self.current_date }")
        print(f'Number of Items: {self.__get_num_items_in_cart()}')

        print(f'Total: ${self.__get_cost_of_cart():.0f}')

        if not self.cart_items:
            print(f'{alert}SHOPPING CART IS EMPTY{reset}')

    def print_descriptions(self):
        """
        Outputs each items description.
        """

        print(f"{self.customer_name}'s Shopping Cart - {self.current_date }")
        print('Item Descriptions')
        for item in self.cart_items:
            print(f'{item.item_name}: {item.item_desc}')

def print_menu(shopping_cart):
    """
    Prints an online shopping menu for the user.
    """

    while True:
        print(f"\n{'-'*20} MENU {'-'*20}")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        
        option = input("Choose an option: ")

        # Create ItemToPurchase object.
        item = ItemToPurchase()

        if option.lower() == 'a':
            # Prompt the user for item details
            print(f"\n{'*'*20} ADD ITEM TO CART {'*'*20}")
            item.item_name = input("\nEnter the item name: ")
            item.item_desc = input('Enter the item description:')
            price = input("Enter the item price: ")
            qty = input("Enter the item quantity: ")

            #item.item_name = item_name
            item.item_price = float(price) if price else 0
            item.item_qty = int(qty) if qty else 0

            shopping_cart.add_item(item)

        elif option.lower() == 'r':
            print(f"\n{'*'*20} REMOVE ITEM FROM CART {'*'*20}")
            # Prompt the user for item to be removed.
            item_name = input("\nEnter name of item to remove: ")
            shopping_cart.remove_item(item_name)

        elif option.lower() == 'c':
            print(f"\n{'*'*20} CHANGE ITEM QUANTITY {'*'*20}")
            # Prompt the user for item details
            name = input("\nEnter the item name: ")
            qty = input("Enter the new quantity: ")

            item.item_name = name
            item.item_qty = int(qty) if qty else 0

            # Change item quantity.        
            shopping_cart.modify_item(item)

        elif option.lower() == 'i':
            # Output items' description.
            print(f"\n{'*'*20} OUTPUT ITEMS' DESCRIPTIONS {'*'*20}")
            shopping_cart.print_descriptions()

        elif option.lower() == 'o':
            # Output shopping cart.
            print(f"\n{'*'*20} OUTPUT SHOPPING CART {'*'*20}")
            shopping_cart.print_total()

        elif option.lower() == 'q':
            break

def validate_date(current_date):
    """
        Checks if the date is entered in the correct format, ex: February 1, 2020
    """
    
    return bool(re.match(r'^([A-Za-z]+) (\d{1,2}), (\d{4})$', current_date))

if __name__ == "__main__":
    try:
        # Initialize an empty shopping cart (list of dictionaries)
        cart = ShoppingCart()

        cart.customer_name = input("Enter customer's name: ")

        current_date = input("Enter today's date: ")
        # Validate the date to ensure it follows the format: February 1, 2020
        if not validate_date(current_date):
            raise DateError("Invalid date format.")

        cart.current_date = current_date

        print(f'Customer name: {cart.customer_name}')
        print(f"Today's date: {cart.current_date}")

        print_menu(cart)
    except (Exception, DateError) as e:
        print(f'Error: {e}')