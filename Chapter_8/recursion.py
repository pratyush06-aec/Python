def fact(n):
    if(n== 0 and n== 1):
        return 1
    return n* fact(n- 1)

n= int(input("Enter a number: "))
print(f"The factorial of: {fact(n)}")