a= int(input("Enter the frst subject's marks: "))
b= int(input("Enter the second subject's marks: "))
c= int(input("Enter the third subject's marks: "))

if((((a+b+c)/3)*100)>= 40):
    print("The student achieved the overall pass percentage")

if(a>= 33 and b>= 33 and c>= 33):
    print("The students has also passed in each subject")
elif(a<33):
    print("Student failed in first subject")
elif(b<33):
    print("Student failed in second exam")
elif(c<33):
    print("Student failed in third exam")
else:
    print("The student failed completely")