import datetime

num = input().split(" ")
x = datetime.datetime(2009,int(num[1]),int(num[0]))
print(x.strftime("%A"))
