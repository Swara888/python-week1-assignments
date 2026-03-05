balance = 1000
correct_pin = 1234

pin = int(input("Enter your PIN: "))

if pin == correct_pin:

    while True:
        print("\nATM Menu")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print("Your balance is:", balance)

        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print("Deposit successful")

        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Withdrawal successful")
            else:
                print("Insufficient balance")

        elif choice == 4:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid option")

else:
    print("Incorrect PIN")
