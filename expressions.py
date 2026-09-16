#AB 7th integers, floats,and expressions

# integer => whole number
people= 23
cars= 50
computers= 29
awarness= 12
grades= 15
#float => numbers with decimals
pi= 3.14159
temp= 95.6
cost= 1.99
rain= 2.17

#arithmic operations +=addition -=subtaction *=multiplication \=division **= exponents %=mod
print(f"18/4 is {18/4} or {18//4} and the remainder is {18%4}")
print(f"18/5 is {18/5} or {18//5} and the remainder is {18%5}")

#order of operations
average=[85,66,94,72,100]
students= len(grades)
avergae= sum(grades/people)

print(f"the average is {int(average)}")

#int=integer float=float str=string. inputs are always strings.

#canvert data type
price=float(input("How much did the item cost: "))
tax= 0.0485
sales_tax=price * tax
total= price + sales_tax

print(f"Your total is {total}")