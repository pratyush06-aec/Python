word= ["Donkey", "Bad", "Ganda"]

with open("replacement.txt") as file:
    content= file.read()

for words in word:
    content_new= content.replace(words, "#"*len(words))

    with open("replacement.txt", "w") as file:
        file.write(content_new)