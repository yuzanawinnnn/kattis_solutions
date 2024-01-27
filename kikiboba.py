s = input()
b = s.count('b')
k = s.count('k')

if(b > k):
    print("boba")
elif(k > b):
    print("kiki")
elif(b == 0 and k == 0):
    print("none")
else:
    print("boki")
