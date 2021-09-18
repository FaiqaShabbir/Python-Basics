# for inside while loop example
print("Do you want to travel:")
travelling = input("Yes or No \n")

while travelling in ('yes', 'YES', 'Yes',):
    num = int(input("Number of people travelling: "))

    for num in range(1, num+1):
        name = input("Name: ")

        age = int(input("Age: "))

        gender = input("Male or Female: ")

        print("Passenger name: ", name)
        print("Passenger age: ", age)
        print("Passenger gender: ", gender)
        print("\n")

    travelling = input("Oops! forgot someone? (-^-) \n ")