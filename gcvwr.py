G = input().split(" ")
item = input().split(" ")
item = list(map(int, item))
        
total = sum(item)

diff = int(G[0]) - int(G[1])
print(int(diff*90/100) - total)
