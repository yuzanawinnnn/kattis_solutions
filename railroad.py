num = int(input())

for j in range(num):
    #if j > 0:
        #print()
    input()
    n, m = map(int, input().split())
    graph = {}
    
    for i in range(1, n+1):
        graph[i] = []

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
        
    to_remove = []
    for station in graph:
        if len(graph[station]) == 2:
            to_remove.append(station)
            
    while to_remove:
        station = to_remove.pop()
    
        (n1, d1), (n2, d2) = graph[station]
        new_dist = d1 + d2
    
        if n1 == n2:  # 👈 it's a loop
            graph[n1].append((n2, new_dist))
        else:
            graph[n1].append((n2, new_dist))
            graph[n2].append((n1, new_dist))
    
        graph[n1] = [(nb, d) for nb, d in graph[n1] if nb != station]
        graph[n2] = [(nb, d) for nb, d in graph[n2] if nb != station]
    
        del graph[station]

    edges = []
    for station in graph:
        for nb, d in graph[station]:
            if station <= nb:  # avoid duplicates
                edges.append((station, nb, d))

    print(len(edges))
    for a, b, d in edges:
        print(a, b, d)
