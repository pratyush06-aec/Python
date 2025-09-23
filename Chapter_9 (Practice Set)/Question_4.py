word= "Donkey"

with open("replacement.txt") as file:
    content= file.read()

content_new= content.replace(word, "######")

with open("replacement.txt", "w") as file:
    file.write(content_new)