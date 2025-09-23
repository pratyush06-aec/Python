# file= open("poems.txt")
# content= file.read()
# if("twinkel" in content):
#     print("Yess!!!")   
# else:
#     print("No!!!")

# file.close()


with open("poems.txt") as file:
    if("twinkel" in "poems.txt"):
        print(file.read())
    else:
        print("Error!!!")

