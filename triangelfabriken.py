answer = ""
for i in range(3):
    angle = int(input())
    if(angle == 90):
        answer = "Ratvinklig Triangel"
    elif(angle > 90):
        answer = "Trubbig Triangel"
        
if(answer == ""):
    print("Spetsig Triangel")
else:
    print(answer)
