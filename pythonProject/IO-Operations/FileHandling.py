file1 = open("Nishit.jpg","rb")
#file1.write("Hello Mr. Nishit ")


file = open("Data","a")
for data in file1:
    file.write(str(data))
file.close()

file = open("Data","r")
print(file.read())
file.close()
file1.close()

