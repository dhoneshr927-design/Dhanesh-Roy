user = "john doe"
password = "1234"

balance = 1000

while True:
    print("Welcome to the ATM!")
    entered_user = input("Please enter your username: ")
    entered_password = input("Please enter your password: ")

    if entered_user == user and entered_password == password:
        print("Login successful!")
        while True:
            print("\nPlease choose an option:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == '1':
                print(f"Your current balance is: ${balance}")
            elif choice == '2':
                amount = float(input("Enter the amount to deposit: "))
                balance += amount
               
                from datetime import datetime
                now = datetime.now()
                date = now.strftime("%Y-%m-%d, %H:%M:%S")
                day = now.strftime("%A")
                print(f'Your Transaction is successfully.on {date}, {day}.')
                print(f"You have deposited ${amount}. Your new balance is: ${balance}")
            elif choice == '3':
                amount = float(input("Enter the amount to withdraw: "))
                if amount > balance:
                         print("Insufficient funds. Please try again.")
                else:
                    receipt = input("Do you want a receipt? (yes/no): ")
                    if receipt.lower() == 'yes':
                        print(f"Receipt: You have withdrawn ${amount}. Your new balance is: ${balance - amount}.")
                    balance -= amount
                    from datetime import datetime
                    now = datetime.now()
                    date = now.strftime("%Y-%m-%d, %H:%M:%S")
                    day = now.strftime("%A")
                    print(f"Your Transaction is successfully.on {date}, {day}.")
                    print(f"You have withdrawn ${amount}. Your new balance is: ${balance}")
            elif choice == '4':
               print("Thank you for using the ATM.See your next time.bye!")
               break
        
    else:
        print("Incorrect username or password. Please try again.")