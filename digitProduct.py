n = input()
product = 1
while product >= 10 or product == 1:
    for i in range(len(n)):
        if(n[i] != "0"):
            product = product * int(n[i])
    if(product >= 10):
        n = str(product)
        product = 1
    else:
        break
print(product)
    
