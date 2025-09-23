marks= int(input("Enter the marks of te student: "))

if(marks>=90 and marks<=100):
    print("The student achieved E+ Grade")
elif(marks>=80 and marks<=89):
    print("The student achieved A+ Grade")
elif(marks>=70 and marks<=79):
    print("The student achieved B+ Grade")
elif(marks>=60 and marks<=69):
    print("The student achieved C+ Grade")
elif(marks>=50 and marks<=59):
    print("The student achieved D+ Grade")
else:
    print("The student failed the exam")