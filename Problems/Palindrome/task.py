sent = input()
c = 0

for i in range(round(len(sent)/2)):
    if sent[i] == sent[(len(sent)-i-1)]:
        c += 1
if c == round(len(sent) / 2):
    print("Palindrome")
else:
    print("Not palindrome")
