n = int(input())
score = {}
import operator

for i in range(n):
    temp = input()
    split = temp.split(" ")
    if(split[0] in score):
        score[split[0]] = score[split[0]] + int(split[1])
    else:
        score[split[0]] = int(split[1])
print(max(score.items(), key = operator.itemgetter(1))[0])
    
        
