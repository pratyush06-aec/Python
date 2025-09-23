content= "Hey, you are amazing"

file= open("my_file(1)", "a")           ## Here, "a" indicates "append", whcih means the content would be added at the end of the content in the mentioned file
file.write(content)
file.close()