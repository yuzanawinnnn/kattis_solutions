n = int(input())
arr = []
hungover = 0
for i in range(n):
    state = input()
    if(i > 0): 
        if(state == "sober" and arr[-1] == "drunk"):
            hungover = hungover + 1
    arr.append(state)
print(hungover)
