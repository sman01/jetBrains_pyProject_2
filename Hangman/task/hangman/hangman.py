import random
print("H A N G M A N")
choices = ['python', 'java', 'kotlin', 'javascript']
selected = random.sample(choices, 1)
s = input("Guess the word:")
if s in selected:
    print("You survived!")
else:
    print("You are hanged!")
