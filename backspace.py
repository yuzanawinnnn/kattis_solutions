text = input()
result = []
for i in range(len(text)):
    if(text[i] == '<' and len(result)>0):
        result.pop()
    else:
        result.append(text[i])
ans = ''.join(result)
print(ans)
