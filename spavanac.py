MM=input("")

arr=MM.split(" ")
hour=int(arr[0])
min=int(arr[1])

if(min==0):
    if(hour==0):
       print(23," ",15)
    else:
       print(hour-1," ",15)
elif(min>=45):
  print(hour," ",min-45)
else:
   temp=45-min
   temp_min=60-temp
   if(hour==0):
       print(23," ",temp_min)
   else:
       print(hour-1," ",temp_min)
