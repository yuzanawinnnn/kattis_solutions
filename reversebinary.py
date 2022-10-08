num = int(input())
binary = bin(num).replace("0b", "")
word=""
for i in range(len(binary)-1,-1,-1):
    word+=binary[i]
print(int(word,2))
    
