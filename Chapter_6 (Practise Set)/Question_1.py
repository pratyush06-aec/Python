a= int(input("Enter the number: "))
b= int(input("Enter the number: "))
c= int(input("Enter the number: "))
d= int(input("Enter the number: "))

if(a>b and a>c and a>d):
    print("A is greatest")
elif(b>a and b>c and b>d):
    print("B is greatest")
elif(c>a and c>b and b>d):
    print("C is greatest")
else:
    print("D is greatest")

