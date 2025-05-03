#!/usr/bin/env python3

"""
CSC500-1: CT (Part 1) - Program to calculate the total amount of meal purchased at a restaurant.

"""

additional_charges = {"sales_tax" : 7,
                      "tip" : 18}
total_sales = {
                "meal_price":[],
                "total":[]
            }

meals_available = int(input('Number of meal available: '))

i = 0
while i < meals_available:
    meal_price = float(input('Enter meal price: '))
    sales_tax = additional_charges['sales_tax'] / 100
    tip = additional_charges['tip'] / 100
    grand_total = meal_price + sales_tax + tip
    total_sales["meal_price"].append(meal_price)
    total_sales["total"].append(grand_total)
    i += 1


total_meal_price = 0
grand_total = 0
print("-"*28)
print(f'|   Meal price  |   Total  |')
print("-"*28)
for count in range(meals_available):
    print(f'|   ${total_sales["meal_price"][count]:.2f}      |   ${total_sales["total"][count]:.2f}  |')
    total_meal_price += total_sales["meal_price"][count]
    grand_total += total_sales["total"][count]

print("="*28)
print(f'|   ${total_meal_price:.2f}      |   ${grand_total:.2f} |') 
print("-"*28)
