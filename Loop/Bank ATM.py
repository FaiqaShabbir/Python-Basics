# ATM BANK MACHINE

print("Welcome to HBL Bank!")
restart = 'Y'
chances = 3
balance = 200.00
while chances >= 0:
    pin = int(input("Please Enter Your 4 digit Pin:"))
    if pin == 1234:
        print("You entered your pin correctly\n")
        while restart not in ('n', 'No', 'no', 'N', 'NO'):
            print("Please Press 1 For Your Balance\n")
            print("Please Press 2 To Make Withdraw\n")
            print("Please Press 3 To Pay in\n")
            print("Please Press 4 To Return Card\n")
            option = int(input("What would you like to choose?"))
            if option == 1:
                print("Your Balance is $", balance, '\n')
                restart = input("Would You like to go Back? ")
                if restart in ('n', 'No', 'no', 'N', 'NO'):
                    print("Thank You!")
                    break
            elif option == 2:
                option2 = 'y'
                withdraw = float(input("How much would you like to withdraw? \n$20/$40/$80/$100/$120/$160/$200"))
                if withdraw in [20, 40, 80, 100, 120, 160, 200]:
                    balance = balance-withdraw
                    print("Now you Bank Balance is $", balance)
                    restart = input("Would You like to go Back? ")
                    if restart in ('n', 'No', 'no', 'N', 'NO'):
                        print("Thank You!")
                        break
                    elif withdraw != [20, 40, 80, 100, 120, 160, 200]:
                        print("Invalid Amount, Please Re-try\n")
                        restart = 'y'
                    elif withdraw == 1:
                        withdraw = float(input("Please Enter Desired amount:"))

            elif option == 3:
                pay_in = float(input("How much would you like Pay In? "))
                balance = balance + pay_in
                print("\nYour Balance is now $", balance)
                restart = input("Would You like to go Back? ")
                if restart in ('n', 'No', 'no', 'N', 'NO'):
                    print("Thank You!")
                    break
            elif option == 4:
                print('Please wait whilst your card is Returned...\n')
                print('Thank you for you service')
                break
            else:
                print("Please Enter b correct number! \n")
                restart = 'y'
    elif pin != '1234':
        print('Incorrect Password')
        chances = chances-1
        if chances == 0:
            print("\nNo more tries!")
            break
