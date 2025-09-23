content= "Harry is a good boy"

file= open("my_file(1)", "w")                ## ("w") is applied only when we are about to write in a file
file.write(content)
file.close()