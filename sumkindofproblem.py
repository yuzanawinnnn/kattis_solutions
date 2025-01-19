n = int(input())

for i in range(n):
    s = input()
    s = s.split(" ")
    
    pos = 0
    odd = 0
    even = 0
    num = 1
    for j in range(1,int(s[1])+1):
        pos = pos + j
        if(num% 2 != 0):
            odd = odd + num
            num = num + 1
        if(num%2 == 0):
            even = even + num
            num = num + 1
    print(i+1, pos, odd, even)
