def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    price (float): Original price of the item
    discount_percent (float): Discount percentage (0-100)
    
    Returns:
    float: Final price after discount if discount is 20% or higher, 
           otherwise original price
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Main program
def main():
    try:
        # Get user input
        original_price = float(input("Enter the original price of the item: $"))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Calculate final price
        final_price = calculate_discount(original_price, discount_percent)
        
        # Display results
        if discount_percent >= 20:
            print(f"\nOriginal Price: ${original_price:.2f}")
            print(f"Discount: {discount_percent}%")
            print(f"Discount Amount: ${original_price * (discount_percent / 100):.2f}")
            print(f"Final Price: ${final_price:.2f}")
        else:
            print(f"\nNo discount applied (discount must be 20% or higher)")
            print(f"Final Price: ${final_price:.2f}")
            
    except ValueError:
        print("Error: Please enter valid numbers for price and discount percentage!")

# Run the program
if __name__ == "__main__":
    main()