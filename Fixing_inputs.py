#AB Fixing user inputs

while True:
    color=input("Tell me a color").strip().capitalize()

if color.isnumeric():
    print("that is a number not a color!")
else:

    print(f"we painted the walls {color}!")