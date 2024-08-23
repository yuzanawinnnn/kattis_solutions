n = input()
n = n.split(' ')
Villa = False
arr = ['?']*int(n[0])
for i in range(int(n[1])):
    s = input()
    s = s.split(' ')
    word = list(s[1])
    for k in range(len(word)):
        if(arr[int(s[0])-1+k] == '?'):
            arr[int(s[0])-1+k] = word[k]
        elif(arr[int(s[0])-1+k] == word[k]):
            pass
        else:
            Villa = True
            break
if Villa == True:
    print('Villa')
else:
    res = ''.join(arr)
    print(res)
            
