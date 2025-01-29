second = int(input())
hour = 0
minu = 0
sec = 0

if(second >= 3600):
    hour = second // 3600
    second = second % 3600
if(second >= 60):
    minu = second // 60
sec = second % 60
    
print(str(hour) + " : " + str(minu) + " : " + str(sec))
