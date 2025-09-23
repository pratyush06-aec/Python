# def main():

#     try:
#         a= int(input("Enter a number: "))
#         print(a)
#         return 

#     except ValueError as v:
#         print("Heeyyy")
#         print(v)
#         return 

#     # finally:
#     print("Hey, I am inside finally!!!!")             ## In this case, the print statement alone won't be printed.

# main()




def main():
    try:
        a= int(input("Enter a number: "))
        print(a)
        return 

    except ValueError as v:
        print("Heyyy!!!")
        print(v)
        return  

    finally:
        print("Hey, I am inside finallyy!!!!")                ## Here, in this case the print statement would be printed because it's inside finally.
main()




## So, the role of finally is expressed inside a function mainly, as in the second case.
## (finally:) would get executed in both cases i.e., if try statement as well as the except statement are correct.   