while True:
    n = int(input())
    if(n == 0):
        break
    maxi = 0
    for i in range(n):
        count = 0
        word = input()
        count = word.count('aa') + word.count('ee') + word.count('ii') + word.count('oo') + word.count('uu') + word.count('yy')
        if(count > maxi):
            maxi = count
            ans = word
        elif(count == maxi):
            ans = word
            
    print(ans)
            
            
        
