fri = input()
n = int(input())
flag = False

for i in range(n):
    name = input()
    if(len(name) == len(fri)):
        ans = sum(1 for a, b in zip(list(fri), list(name)) if a != b)
        if ans == 1:
            print(i+1)
            flag = True
            break

if(flag == False):
    print(n)
