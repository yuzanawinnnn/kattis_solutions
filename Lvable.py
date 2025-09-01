input()
s = input()
if "lv" in s:
    print(0)
elif "l" in s and s.index("l") != len(s) -1 or "v" in s and s.index("v") != 0:
    print(1)
elif "l" in s and s.index("l") == len(s) -1 or "v" in s and s.index("v") == 0:
    print(2)
else:
    print(2)
    
