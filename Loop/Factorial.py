# Factorial

num = int(input("Enter number: "))
factorial = 1
if num < 0:
    print("Kindly! Enter Positive Number:")
elif num == 0:
    print("Factorial of 0! is 1")
else:
    # here num+1 shows that the number will be execute to the extent of num
    for i in range(1, num+1):
        factorial = factorial*i
print(factorial)
