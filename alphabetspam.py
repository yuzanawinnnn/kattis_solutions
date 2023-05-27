line = input()
lower = 0
upper = 0
symbols = 0
white = 0
length = len(line)
for i in range(len(line)):
    if(line[i].islower()):
        lower= lower + 1
    elif(line[i].isupper()):
        upper = upper + 1
    elif(line[i]=='_'):
        white = white +1
    else:
        symbols = symbols +1
print(white/length)
print(lower/length)
print(upper/length)
print(symbols/length)
