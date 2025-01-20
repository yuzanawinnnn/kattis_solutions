N = int(input())

for i in range(N):
    s = input()
    s = s.split(" ")
    count = int(s[0])
    s = list(map(int, s[1:]))
    avg = sum(s)/count
    arr = [j for j in s if j > avg]
    per = (len(arr)/count) * 100
    print("{:.3f}".format(per)+"%")
    
    
