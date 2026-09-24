#AB 7th password checker

password=input("What is your password: ")
letter=False
symbol=False
upppercase=False
lowercase=False
number=False
for letter in password:
    if len(password):
        length=True

if letter .isupper():
    upppercase=True

if letter .islower():
    lowercase=True

if letter .isnumeric():
    number=True

if letter in ("!@#$%^&*()-_=+{[]}/;:~`"):
    symbol=True