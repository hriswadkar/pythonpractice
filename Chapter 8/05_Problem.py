def Pattern(n):
    if (n == 0):
        return
    print ("*" * n)
    Pattern(n - 1)


Pattern(5)