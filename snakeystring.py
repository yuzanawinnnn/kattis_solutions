n = input().split()
snake = []
s = ""
for k in range(int(n[0])):
    temp = input()
    snake.append(temp)
    

for i in range(int(n[1])):
    for j in range(int(n[0])):
        if(snake[j][i] != "."):
            s = s + snake[j][i]

print(s)
