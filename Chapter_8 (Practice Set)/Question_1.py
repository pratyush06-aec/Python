def greatest():
    x= int(input("Enter the number: "))
    y= int(input("Enter the number: "))
    z= int(input("Enter the number: "))

    if(x>y and x>z):
        return x
    elif(y>x and y>z):
        return y
    else:
        return z

print(f"The greatest number is: " , {greatest()})