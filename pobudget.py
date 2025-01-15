N = int(input())
revenue = 0
expense = 0

for i in range(N):
    s = input()
    m = int(input())
    
    if(m <= 0):
        expense = expense + m
    else:
        revenue = revenue + m
        
if(abs(revenue) - abs(expense) == 0):
    print("Lagom")
elif(abs(revenue) - abs(expense) > 0):
    print("Usch, vinst")
else:
    print("Nekad")
