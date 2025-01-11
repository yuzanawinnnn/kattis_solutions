s = input()
s = s.split(" ")


while (all(s[i] <= s[i+1] for i in range(len(s) - 1)) != True):
    for i in range(len(s)-1):
        if(s[i] > s[i+1]):
            temp = s[i+1]
            s[i+1] = s[i]
            s[i] = temp
            ss = ' '.join(s)
            print(ss)
