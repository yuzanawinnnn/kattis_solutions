n = input()
n = n.split(" ")
first = 0
second = 0

for i in range(int(n[0])):
    c = input()
    content = c.split(" ")
    first = first + int(content[0]) * int(content[1])
    
    
for i in range(int(n[1])):
    c = input()
    content = c.split(" ")
    second = second + int(content[0]) * int(content[1])
    
if(first == second):
    print("same")
else:
    print("different")
