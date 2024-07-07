ppl = int(input())
cash = input()
cash = cash.split(" ")
total = sum(list(map(int, cash)))
if(total%3 == 0):
    print("yes")
else:
    print("no")
