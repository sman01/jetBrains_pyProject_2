import random
print("H A N G M A N\n")
choices = ['python', 'java', 'kotlin', 'javascript']
selected = random.sample(choices, 1)
sele = selected[0]
g = 0
se = set()
i = 0
s = ""
op = list(sele)
bs = [None] * len(op)
tr = [None] * len(op)
while i < 8:
    for j in range(len(op)):
        if op[j] == s and tr[j] is None:
            bs[j] = s
            tr[j] = 1
        elif tr[j] is None:
            bs[j] = "-"

    if i < 8:
        print()
        print(''.join(bs))
    s = input("Input a letter: ")
    if len(s) > 1 or len(s) == 0:
        print("You should input a single letter\n")
        continue
    elif ord(s) not in range(97, 123):
        print("It is not an ASCII lowercase letter\n")
        continue
    elif s in se:
        print("You already typed this letter\n")
        continue
    elif s not in sele:
        i += 1
        print("No such letter in the word")

    if s not in se:
        se.add(s)

if "-" not in bs:
    print("You guessed the word ".join(bs) + "!")
    print("You survived!")
else:
    print("You are hanged!")




