n = int(input())
items = []
count = 0
for i in range(n):
    item = input()
    items.append(item)
if("keys" not in items):
    print("keys")
    count = count + 1
if("phone" not in items):
    print("phone")
    count = count + 1
if("wallet" not in items):
    print("wallet")
    count = count + 1
if(count == 0):
    print("ready")
