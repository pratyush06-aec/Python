## Removing a word from the list and returning a new list.

# def rem(l, word):
#     for item in l:
#         l.remove(word)
#         return l

# l=["Harry", "Rohan", "Subham", "an"]
# print(rem(l, "an"))



## Stripping a word from the list and returning a new list.

def rem(l, word):
    n=[]
    for item in l:
        if(item!= word):
            n.append(item.strip(word))
    return n
    
l=["Harry", "Rohan", "Subham", "an"]
print(rem(l, "an"))


