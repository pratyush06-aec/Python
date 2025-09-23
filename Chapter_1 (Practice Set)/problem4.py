import os

# Print the content of the current directory
# for item in os.listdir('.'):
#     print(item)

import os
directory= '.'
contents= os.listdir(directory)
for item in contents:
    print(item)


