#AB, Loops Notes
import random

count=1

while count <= 100000000000000000000000000:
    print(count)
    count+=1


ducks=1
goose=random.randint(1,11)

while True:
    if ducks==goose:
        break
    print('duck....')
    ducks=+1
print('GOOSE!')


sibilings=["alex", "kaitie", "andrew", "tia", "treyson", "xaivier", "jake"]
print(sibilings[2])
sibilings.append("jeyshnee")
sibilings.insert(3, "vienna")
print(sibilings)
sibilings.pop(3)
print(sibilings)
for sibilings in sibilings:
    print(sibilings)

for num in range(1,11,3):
    print(num)

for num in range(1,25):
    if num% 15 == 0:
        print("fizbuzz")
    elif num