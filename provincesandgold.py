num=input().split(" ")
total_cash=3*int(num[0])+2*int(num[1])+1*int(num[2])

if(total_cash>=8):
    print("Province or Gold")
elif (total_cash>=6):
    print("Duchy or Gold")
elif(total_cash>=5):
    print("Duchy or Silver")
elif(total_cash>=3):
    print("Estate or Silver")
elif(total_cash>=2):
    print("Estate or Copper")
else:
    print("Copper")
