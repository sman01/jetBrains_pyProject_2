import random
print("H A N G M A N\n")
choices = ['python', 'java', 'kotlin', 'javascript']
selected = random.sample(choices, 1)
sele = selected[0]
g = 0
b = "-" * len(sele)
print(b)
op = list(sele)
bs = [None] * len(op)
tr = [None] * len(op)
for i in range (8):
    s = input("Input a letter:")
    if s not in sele:
        print("No such letter in the word")
    for i in range(len(op)):
        if op[i] == s and tr[i] == None:
            bs[i] = s
            tr[i] = 1
        elif tr[i] == None:
            bs[i] = "-"
    print()

    print(''.join(bs))
print("Thanks for playing!\nWe'll see how well you did in the next stage")




