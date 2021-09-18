def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num - 1)


def pal(n):
    # Slice notation : So, when you do a[::-1], it starts
    # from the end towards the first taking each element.
    # So it reverses a.
    # This is applicable for lists/tuples as well.
    x = n[::-1]
    if x == n:
        return f"{x} Is Palindrome"
    else:
        return "Not palindrome"
