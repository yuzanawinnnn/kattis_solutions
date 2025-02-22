city = input()
per = float(input())
n = int(input())
non = 0

for i in range(n):
    item = input()
    if (item == "ekki plast"):
        non = non + 1

res = non/n
if(res > per):
    print("Neibb")
else:
    print("Jebb")
