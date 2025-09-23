with open("my_file.txt") as file:
    content1= file.read()

with open("my_file_copy.txt") as file:
    content2= file.read()

if(content1== content2):
    print("Yes, these files are identical!!!!")
else:
    print("No, these files are not identical!!!")