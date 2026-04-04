n = int(input())
for i in range(n):
    name = input()
    abb = input()
    j = 0
    while True and j <len(abb):
        if abb[j] not in name:
            break
        j = j + 1
    if j < len(abb):
        print("NO")
    else:
        print("YES")
