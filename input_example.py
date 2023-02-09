name = input("What is your name? ")
age = input("How old will you be this year? ")
try:
    age = int(age)
    birth_year = 2023 - age
except ValueError:
    print("sorry, that was not a valid number")
except NameError:
    print("oh, it's not you it's me :)")
else:
    print(name, "you were born in", age)
finally:
    print('thank you for playing, come again!')
