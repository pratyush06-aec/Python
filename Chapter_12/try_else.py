try:
    a= int(input("Enter a number: "))
    print(a)

except ValueError as v:
    print("Heyyy!!!!")
    print(v)

else:
    print("The code executed successfully!!!!")