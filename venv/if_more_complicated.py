try:
    a = int(input("give me a number pls "))
    b = int(input("give me another number pls "))
except ValueError:
    print("one of the number was invalid")
    exit (1)
if a > b:
    print(a, ">", b)
elif a < b:
    print(a, "<", b)
else:
    print(a, "=", b)

