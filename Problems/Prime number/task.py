no = int(input())
i = 1
if no == 1 or no == 0:
    print("This number is not prime")
for i in range(2, no):
    if no % i == 0:
        print("This number is not prime")
        break
if i == no - 1:
    print("This number is prime")
