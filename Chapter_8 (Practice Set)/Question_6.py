def convert(i):
    return (i*2.54)

i= float(input("Enter the length: "))
c= convert(i)
print(f"The length in centimeters is: {round(c, 2)}cm")