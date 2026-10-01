#AB 7th READING

with open("7th/practice.txt", "r") as file:
    content= file.read()
    content=content + "\nwinnie the pooh"
    print(content)

with open("7th/practice.txt", "w")as file:
    file.write("Winnie the pooh and the blustery day")