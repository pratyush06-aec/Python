p1= "Make a lot of money"
p2= "buy now"
p3= "subscribe this"
p4= "click this"

m= input("Enter your  message: ")

if(p1 in m or p2 in m or p3 in m or p4 in m):
    print("You are being spammed")
else:
    print("You are free to move on")