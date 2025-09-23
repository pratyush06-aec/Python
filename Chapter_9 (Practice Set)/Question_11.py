import os                                      ## os is a module which here, was used for removing/deleting a file named "game.txt"

with open("game.txt") as file:
    content= file.read()

with open("my_file.txt", "w") as file:
    file.write(content)

os.remove("game.txt")