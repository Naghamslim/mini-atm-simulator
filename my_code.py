balance = 1000
exit_program = False

print("Welcome to the ATM")
print("Your balance is",balance)

while not exit_program:
    print("1. Check the balance.")
    print("2. Deposit Money.")
    print("3. WithDraw Money.")
    print("4. Exit")

    op = int(input("Choose an option:"))

    if op == 1:
        print("Your balance is",balance)
    elif op == 2:
        deposit_amount= int(input("Enter amount to deposit:"))
        balance = balance + deposit_amount
        print("The new balance:",balance)
    elif op == 3:
        withdraw_amount = int(input("Enter amount to withDraw:"))
        new_balance = balance - withdraw_amount
        if new_balance >= 0:
            print("WithDrawal successful. New balance =",new_balance)
        else:
            print("Insufficient funds!")
    elif op == 4:
        print("Goodbye!") 
        exit_program =True
    else:
        print("Invalid option. Please choose 1-4.")
