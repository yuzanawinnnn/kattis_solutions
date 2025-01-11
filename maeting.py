n = input()
s = ""

monday = input()
monday = monday.split(" ")

tuesday = input()
tuesday = tuesday.split(" ")

for i in range(len(monday)):
    if(monday[i] in tuesday):
        s = s + monday[i] + " "
    
print(s[:len(s)-1])
