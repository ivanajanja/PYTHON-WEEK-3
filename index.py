def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): The original price of the item. Must be non-negative.
        discount_percent (float): The discount percentage. Must be between 0 and 100.

    Returns:
        float: The final price after the discount is applied, or the original
               price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price


def main():
    """
    Prompts the user for price and discount percentage, validates inputs,
    calculates and prints the final price.
    """
    try:
        # Prompt the user to enter the original price
        original_price = float(
            input("Enter the original price of the item (non-negative): "))
        if original_price < 0:
            print("Error: Price cannot be negative.")
            return

        # Prompt the user to enter the discount percentage
        discount_percentage = float(
            input("Enter the discount percentage (0-100): "))
        if not (0 <= discount_percentage <= 100):
            print("Error: Discount percentage must be between 0 and 100.")
            return

        # Calculate the final price using the function
        final_price = calculate_discount(original_price, discount_percentage)

        # Print the result based on whether a discount was applied
        if final_price < original_price:
            print(f"\nDiscount of {discount_percentage}% applied!")
            print(f"The final price is: ${final_price:.2f}")
        else:
            print(
                f"\nNo discount was applied because the discount percentage was less than 20%.")
            print(f"The original price remains: ${original_price:.2f}")

    except ValueError:
        print("Invalid input. Please enter numerical values for price and discount percentage.")


if __name__ == "__main__":
    main()
