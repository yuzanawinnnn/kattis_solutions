first = input()
second = input()
count = 0
for i in range(len(first)):
    if(first[i] != second[i]):
        count = count + 1
print(count + 1)
