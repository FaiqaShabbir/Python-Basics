# Pyramid

def pattern(n):
    # For Blank spaces take k
    k = 2 * n - 2
    # i for number of inner rows
    for i in range(0, n):
        # j for number of outer columns
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        # Moving Forward Direction
        for j in range(0, i + 1):
            print("^ ", end="")
        print("\r")


pattern(10)


# Pyramid

def pattern1(n):
    # For Blank spaces take k
    k = n - 2
    # i for number of inner rows
    for i in range(n, -1, -1):
        # j for number of outer columns
        # range(start, stop, step)
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        # Moving Forward Direction
        for j in range(0, i + 1):
            print("v ", end="")
        print("\r")

pattern1(10)
