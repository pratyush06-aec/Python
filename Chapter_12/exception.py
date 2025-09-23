try:
    a= int(input("Enter a number: "))
    print(a)

except TypeError as t:
    print("Hello")
    print(t)

except ValueError as v:
    print("Hiii")
    print(v)

except Exception as e:
    print("Heyy")
    print(e)