book = int(input())
n = []
for i in range(book):
    price = int(input())
    n.append(price)

n.sort(reverse = True)
#print("reverse", n)

m = 0
total = 0
while m < len(n):
    arr = [n[m]]
    if(m < len(n)-1):
        arr.append(n[m+1])
    if(m < len(n)-2):
        arr.append(n[m+2])
    if(len(arr) == 3):
        arr= arr[:len(arr)-1]
    total += sum(arr)
    m = m + 3
    
print(total)
