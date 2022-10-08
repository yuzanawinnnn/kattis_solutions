num=int(input())
while(num!=-1):
  
  total = 0
  value=0
  for i in range(num):
      temp = input().split(" ")
      if(i==0):
          total+= int(temp[0])*int(temp[1])
          value = int(temp[1])
      else:
          total+=int(temp[0])*(int(temp[1])-value)
          value = int(temp[1])
  print(total,"miles") 
  num=int(input())
       
