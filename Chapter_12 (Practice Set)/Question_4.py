# a= int(input("Enter the first number: "))
# b= int(input("Enter the second number: "))

# if(b==0):
#     raise ZeroDivisionError("Hey, Our program doesn't support divisio by zero!!!")
   
# else:
#     print(a/b)


try:
    a= int(input("Enter a: "))
    b= int(input("Enter b: "))

    print(a/b)
    
except ZeroDivisionError as z:
    print("Heyyyy!!!!!")


