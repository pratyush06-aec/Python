## (global a) changes the global variable and gives the value equals to the local variable.
## In first case, a= 3 is the local variable(of the function itself) and a= 50 is the global variable.



# a= 50

# def show():
#     a= 3
#     print(a) 
    
# show()
# print(a)



a= 40

def main():
    global a
    a= 5
    print(a)

main()
print(a)