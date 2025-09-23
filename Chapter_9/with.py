## If we apply "with" statement, we would'nt be required to write file.close() at the end


with open("my_file.txt") as file:
    print(file.read())


## Instead of:


file= open("my_file.txt")
print(file.read())
file.close()