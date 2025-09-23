with open("my_file.txt") as file:
    lines= file.readlines()

line_no= 1
for line in lines:
    if("python" in line):
        print(f"Yes, python is present in: {line_no} !!!!")
        break
    line_no+= 1
else:
    print("No, python is not present in the lines!!!!")