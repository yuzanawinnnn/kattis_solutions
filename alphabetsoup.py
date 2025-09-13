s = input()
import string
ss = ""

uppercase_alphabets = list(string.ascii_uppercase)
for i in range (len(uppercase_alphabets)):
    if uppercase_alphabets[i] not in s:
        ss = ss +uppercase_alphabets[i] 
if len(ss) == 0:
    print("Alphabet Soup!")
else:
    print(ss)
