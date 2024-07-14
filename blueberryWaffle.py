n = input()
n = n.split(" ")
turn = round(int(n[1])/int(n[0]))
if(turn%2 == 0):
    print("up")
else:
    print("down")
