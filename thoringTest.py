n = int(input())
words = []
found = False
for i in range(n):
    temp = input()
    words.append(temp.lower())
AI = input()
AI = AI.split(" ")
for j in range(len(AI)):
    if(AI[j].lower() not in words):
        print("Thore has left the chat")
        found = True
        break
if found == False:
    print("Hi, how do I look today?")
    
    
