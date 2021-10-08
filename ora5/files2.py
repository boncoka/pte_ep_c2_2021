fileobject1 = open("lorem.txt", "r")
fileobject2 = open ("lorem_copy.txt", "w")
fileobject3 = open("loerem_copy2.txt", "w")
for line in fileobject1:
    new_row = ""
    for character in line:
        if character != " ":
            new_row = new_row + character
        else:
            new_row = new_row + " "
    fileobject2.write(line)
    fileobject3.write(line.replace(" ", "   "))
fileobject1.close()
fileobject2.close()