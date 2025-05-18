#!/usr/bin/env python3

import calendar

def rainfall_calculator():

    # Get the number of years 
    num_of_years = int(input('Enter the number of years: '))
    if num_of_years <= 0:
        print('Invalid input. Please enter a whole number.')
        exit()

    num_of_months = 0
    total_rainfall = 0.0
    average_rainfall = 0.0

    # Collect the rainfall data
    for yr in range(1, num_of_years + 1):
        print(f'\n----Year {yr}----')

        for month in range(1, 12 + 1):
            month_name = calendar.month_name[month]
            
            rainfall =  float(input(f'Enter rainfall (in inches) for {month_name}: '))

            if rainfall < 0:
                print('Rainfall cannot be negative.')
                exit()
            
            # Calculate total months and total rainfall.
            num_of_months += 1
            total_rainfall += rainfall

    # Calculate the average rainrall.
    average_rainfall = total_rainfall / num_of_months

    print('\n---- Rainfall summary ----')

    print(f'Total number of months: {num_of_months}')
    print(f'Total inches of rainfall: {total_rainfall:.2f}')
    print(f'Average rainfall per month: {average_rainfall:.2f} inches')

if __name__ == "__main__":
    rainfall_calculator()

