s = input()
s = s.split(" ")
if int(s[0]) > int(s[2]): 
    print(">")
elif int(s[0]) < int(s[2]):
    print("<")
else:
    print("Goggi svangur!")
