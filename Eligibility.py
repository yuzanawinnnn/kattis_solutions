num = int(input())
for i in range(num):
    student = input()
    student = student.split(" ")
    if(int(student[1][:4]) >= 2010 or int(student[2][:4]) >= 1991):
        print(student[0], "eligible")
    elif(int(student[3]) >= 41):
        print(student[0], "ineligible")
    else:
        print(student[0], "coach petitions")
        
