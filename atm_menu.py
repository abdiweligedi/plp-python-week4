balance = 1000
correct_pin = "1234"

pin = input("Enter your 4-digit PIN: ")

# Check if the PIN entered by the user is correct.
if pin != correct_pin:
    print("Incorrect PIN")
else:
    amount = int(input("How much would you like to withdraw? "))

    # Check if the withdrawal amount is less than or equal to the balance.
    if amount <= balance:
        balance = balance - amount
        print(f"Withdrawal successful. Your new balance is: {balance}")
    else:
        print("Insufficient funds")