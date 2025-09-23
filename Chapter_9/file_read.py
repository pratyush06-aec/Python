file= open("my_file.txt", "r")            ## This ("r") may or maynot be used, as the very next line instructs the compiler to read the mentioned file.                
content= file.read()
print(content)
file.close()

