#creatd By Elliott
#Created on 05/13/2026
# This program asks the user for a positive integer and then it prints the multiplication table for that number from 10 to 20 using a while loop.
def main():
    # 1. Ask the user for a positive integer
    # I used int() to convert the input string into a number/integer
    user_num = int(input("Enter a positive integer: "))

    # 2. Checks if the number is positive
    if user_num <= 0:
        print("Error: Please enter a number greater than 0.")
    else:
        # 3. Initialize the counter at 10 (start of our range)
        counter = 10
        
        print(f"Multiplication Table for {user_num} (10 to 20):")
        print("-" * 30)  # Prints a separator line for better readability

        # 4. Use a while loop to print the table from 10 to 20
        while counter <= 20:
            result = user_num * counter
            print(f"{user_num} x {counter} = {result}")
            
            # 5. Increment the counter to move to the next number
            counter += 1

# Run the program
if __name__ == "__main__":
    main()