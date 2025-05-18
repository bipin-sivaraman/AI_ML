#!/usr/bin/env python3

def point_calculator(item):

    points = 0

    if item > 1 and item < 4:
        points = 5
    elif item > 3 and item < 6:
        points = 15
    elif item > 5 and item < 8:
        points = 30
    elif item > 7:
        points = 60

    return points

if __name__ == "__main__":

    # Get user input. 
    num_of_books = int(input("Enter number of books purchased: "))

    # Validate the input.
    if num_of_books < 0:
        print("Invalid entry. Please enter a whole number.")
        exit()

    # Display the number of points received.
    print(f'Total Points received: {point_calculator(num_of_books)}')

