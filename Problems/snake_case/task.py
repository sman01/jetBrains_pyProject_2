string = input()
fini = ""
for i in range(len(string)):
    if string[i].isupper():
        fini += "_"
        fini += string[i].lower()
    else:
        fini += string[i]
print(fini)

