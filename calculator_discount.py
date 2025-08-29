def calculator_program():
    """
    Simple calculator that performs basic arithmetic operations.
    """
    print("Simple Calculator")
    print("-----------------")
    
    # Get user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ").strip()
        
        # Perform the operation
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid operation! Please use +, -, *, or /.")
            
    except ValueError:
        print("Error: Please enter valid numbers!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the calculator
if __name__ == "__main__":
    calculator()

def demonstrate_list_operations():
    """
    Demonstrates various list operations in Python.
    """
    print("List Operations Demonstration")
    print("---------------------------")
    
    # Create an empty list called my_list
    my_list = []
    print(f"Initial empty list: {my_list}")
    
    # Append elements: 10, 20, 30, 40
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    print(f"After appending 10, 20, 30, 40: {my_list}")
    
    # Insert the value 15 at the second position
    my_list.insert(1, 15)
    print(f"After inserting 15 at position 2: {my_list}")
    
    # Extend with another list: [50, 60, 70]
    my_list.extend([50, 60, 70])
    print(f"After extending with [50, 60, 70]: {my_list}")
    
    # Remove the last element
    last_element = my_list.pop()
    print(f"After removing last element ({last_element}): {my_list}")
    
    # Sort in ascending order
    my_list.sort()
    print(f"After sorting in ascending order: {my_list}")
    
    # Find and print the index of the value 30
    try:
        index_30 = my_list.index(30)
        print(f"The index of value 30 is: {index_30}")
    except ValueError:
        print("Value 30 not found in the list")
    
    # Final state of the list
    print(f"Final my_list: {my_list}")

# Run the list operations demonstration
if __name__ == "__main__":
    demonstrate_list_operations()

    def calculate_discount(price, discount_percent):
    """
 


 
 


 

    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

def main():
    """
    Main function to interact with the user and calculate discounts.
    """
    print("Discount Calculator")
    print("------------------")
    
    try:
        # Get user input
        original_price = float(input("Enter the original price of the item: $"))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Validate inputs
        if original_price < 0:
            print("Error: Price cannot be negative!")
            return
        if discount_percent < 0 or discount_percent > 100:
            print("Error: Discount percentage must be between 0 and 100!")
            return
        
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

 # Python Programming Projects

This repository contains three simple Python programs that demonstrate basic programming concepts including user input handling, list operations, and function implementation.

## 📋 Project Overview

### 1. Simple Calculator
A program that performs basic arithmetic operations based on user input.

### 2. List Operations
A program demonstrating various list manipulation techniques in Python.

### 3. Discount Calculator
A function-based program that calculates final prices after applying discounts.

## 🎯 Objectives

- Practice basic Python syntax and control structures
- Demonstrate user input handling and validation
- Implement list operations and manipulations
- Create reusable functions with conditional logic
- Provide clear documentation and error handling

## 🛠️ Tools and Libraries Used

- **Python 3.x** (No external libraries required)
- Built-in functions: `input()`, `print()`, `float()`, `try-except`
- List methods: `append()`, `insert()`, `extend()`, `pop()`, `sort()`, `index()`


