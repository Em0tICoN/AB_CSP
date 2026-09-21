#AB Fixing user inputs

while True:
    color=input("Tell me a color").strip().capitalize()

if color.isnumeric():
    print("that is a number not a color!")
else:

    print(f"we painted the walls {color}!")


while True:
     try:
        income=float(input("what is your rent?: "))
        break
     except:
         print("This is not what I asked for.")

while True:
     try:
        income=float(input("what is your monthly utillities?: "))
        break
     except:
         print("This is not what I asked for.")

while True:
     try:
        income=float(input("what is your monthly groceries?: "))
        break
     except:
         print("This is not what I asked for.")
