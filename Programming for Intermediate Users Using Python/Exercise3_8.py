#1
newfile = open("newfile.txt", "r")
#2
print(newfile.read())
#3
print(newfile.readline())
#4
for x in newfile:
    print(x)

#5
import os
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
      os.remove("newfile.txt")
