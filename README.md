Discount Calculator
Overview

This Python program calculates the final price of an item after applying a discount based on user input. It only applies the discount if the discount percentage is 20% or higher; otherwise, it returns the original price.

Features

Prompts the user to input the original price and discount percentage.

Validates input to ensure price is non-negative and discount percentage is between 0 and 100.

Calculates and displays the discounted price if applicable.

Provides informative messages for invalid inputs and when no discount is applied.

Usage

Run the script.

When prompted, enter the original price of the item (must be zero or positive).

Enter the discount percentage (a value between 0 and 100).

The program will display the final price after discount if the discount is 20% or more.

If the discount is less than 20%, the original price will be shown with a message stating no discount was applied.

Example
Enter the original price of the item (non-negative): 150
Enter the discount percentage (0-100): 25

Discount of 25% applied!
The final price is: $112.50

Requirements

Python 3.x

How to Run
python discount_calculator.py

Notes

The program handles invalid inputs gracefully and prompts the user to provide valid numerical values.

No external libraries are required.# PYTHON-WEEK-3
