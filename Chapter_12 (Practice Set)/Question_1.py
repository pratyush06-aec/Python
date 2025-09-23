# try:
#     with open("file1.txt") as f1, open("file2.txt") as f2, open("file3.txt") as f3:
#         print(f1.read())
#         print(f2.read())
#         print(f3.read())

# except Exception as e:
#     print("Heyyy!!!!!")
#     print(e)

# else:
#     print("It's working perfectly fine!!!!")



try:
    with open("file1.txt") as f1:
        print(f1.read())
    
except Exception as e:
    print("Heyyyy")
    print(e)

else:
    print("It's working perfectly fine!!!!")

try:
    with open("file2.txt") as f2:
        print(f2.read())

except Exception as e:
    print("Heyyyy")
    print(e)

else:
    print("It's working perfectly fine!!!!")

try:
    with open("file3.txt") as f3:
        print(f3.read())

except Exception as e:
    print("Heyyyy")
    print(e)
    
else: 
    print("It's working perfectly fine!!!")


