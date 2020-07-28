import random
print("H A N G M A N\n")
choices = ['python', 'java', 'kotlin', 'javascript']
selected = random.sample(choices, 1)
sele = selected[0]
g = 0
se = set()
b = "-" * len(sele)
print(b)
i = 0
op = list(sele)
bs = [None] * len(op)
tr = [None] * len(op)
while i < 8:
    s = input("Input a letter:")
    if s not in sele:
        i += 1
        print("No such letter in the word")
    if s in se and s in sele:
        i += 1
        print("No improvements")
    elif s not in se:
        se.add(s)
    for j in range(len(op)):
        if op[j] == s and tr[j] is None:
            bs[j] = s
            tr[j] = 1
        elif tr[j] is None:
            bs[j] = "-"

    if i < 8:
        print()
        print(''.join(bs))
if "-" not in bs:
    print("You guessed the word")
    print("You survived!")
else:

    print("You are hanged!")




