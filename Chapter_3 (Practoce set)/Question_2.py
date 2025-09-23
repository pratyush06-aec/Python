# name= str(input("Enter your name: "))
# # date= int(input("Enter the date: "))
# print(f"""Dear, {name} \nYou are selected \n27/04/2025""")


letter= """Dear <|NAME|>,
You are selected
Date: <|DATE|>
"""
print(letter.replace("<|NAME|>", "Pratyush").replace("<|DATE|>", "27 september 2025"))    ## This way of using replace fucntion is called chaining.