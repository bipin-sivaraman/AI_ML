#!/usr/bin/env python3

"""
CSC500-1: CT (Part 1) - Program to calculate the total amount of meal purchased at a restaurant.

"""

additional_charges = {"sales_tax" : 7,
                      "tip" : 18}
total_sales = {
                "meal_price":[],
                "sales_tax":[],
                "tip":[],
                "total":[]
            }

meals_available = int(input('Number of meal available: '))

i = 0
while i < meals_available:
    meal_price = float(input('Enter meal price: '))
    sales_tax = meal_price * additional_charges['sales_tax'] / 100
    tip = meal_price * additional_charges['tip'] / 100
    grand_total = meal_price + sales_tax + tip
    total_sales["meal_price"].append(meal_price)
    total_sales["sales_tax"].append(sales_tax)
    total_sales["tip"].append(tip)
    total_sales["total"].append(grand_total)
    i += 1


total_meal_price = 0
total_sales_tax = 0
total_tip = 0
grand_total = 0
print("-"*55)
print(f'|{" "*3}Meal price{" "*3}|{" "*3}Sale tax{" "*3}|{" "*3}Tip{" "*3}|{" "*3}Total{" "*3}|')
print("-"*55)
for count in range(meals_available):
    print(f'|{" "*5}${total_sales["meal_price"][count]:.2f}{" "*5}|{" "*5}${total_sales["sales_tax"][count]:.2f}{" "*4}', end='')
    print(f'|{" "*2}${total_sales["tip"][count]:.2f}{" "*2}|{" "*3}${total_sales["total"][count]:.2f}{" "*2}|')
    total_meal_price += total_sales["meal_price"][count]
    total_sales_tax += total_sales["sales_tax"][count]
    total_tip += total_sales["tip"][count]
    grand_total += total_sales["total"][count]

print("="*55)
print(f'|{" "*5}${total_meal_price:.2f}{" "*5}|{" "*5}${total_sales_tax:.2f}{" "*4}|{" "*2}${total_tip:.2f}{" "*2}|{" "*3}${grand_total:.2f}{" "*2}|') 
print("-"*55)
