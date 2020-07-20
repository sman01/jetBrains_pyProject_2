begin = int(input())
end = int(input())
sum = 0
len = 0
for i in range(begin, end+1):
    if i % 3 == 0:
        sum += i
        len += 1
print(sum / len)
