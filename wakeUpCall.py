input()
s1 = sum(map(int, input().split()))
s2 = sum(map(int, input().split()))
print("Button 1" if s1 > s2 else "Button 2" if s2 > s1 else "Oh no")

