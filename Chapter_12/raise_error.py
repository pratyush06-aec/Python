a= int(input("Enter a number: "))
b= int(input("Enter a number: "))

if(b==0):
    raise ValueError("Hey, Our program is not meant to divide a number by zero!!!")

else:
    print(f"The result of(a/b) is: {a/b}")