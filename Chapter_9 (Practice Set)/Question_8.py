with open("my_file.txt") as file:
    content= file.read()

with open("my_file_copy.txt", "w") as file:
    file.write(content)