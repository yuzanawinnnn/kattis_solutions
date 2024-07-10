n = int(input())
absent = []
student = input()
for i in range(1,n):
    voice = input()
    if(voice != 'Present!' and student != 'Present!'):
        absent.append(student)
    student = voice
if(student != 'Present!'):
    absent. append(student)
if(len(absent) ==0):
    print("No Absences")
else:
    for j in range(len(absent)) :
        print(absent[j])
