n = int(input())
count = []
category = []
all_win = []
final = []
for i in range(n):
    costume = input()
    if(costume in category):
        count[category.index(costume)] = count[category.index(costume)]+1
    else:
        count.append(1)
        category.append(costume)
win = min(count)
if(count.count(win) == 1):
    print(category[count.index(win)])
else:
    for k in range(len(count)):
        if(count[k] == win):
            all_win.append(k)
for j in range(len(all_win)):
    final.append(category[all_win[j]])
final.sort()
for l in range(len(final)):
    print(final[l])
    
