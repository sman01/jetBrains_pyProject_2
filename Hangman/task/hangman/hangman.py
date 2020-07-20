import random
print("H A N G M A N")
choices = ['python', 'java', 'kotlin', 'javascript']
selected = random.sample(choices, 1)
sele = selected[0]
sel = sele[:3]
b = "-" * (len(sele) - 3)
s = input(f"Guess the word: {sel}{b}")
if s in selected:
    print("You survived!")
else:
    print("You are hanged!")
