N = int(input()) #problems
M = int(input()) # teams
P = input()
P = P.split(" ")
score = [0] * N

for i in range(M):
    points = input()
    points = points.split()
    for j in range(N):
        score[j] = score[j] + int(points[j])

print(P[score.index(max(score))])
