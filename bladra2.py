
 Download bladra2.py
s = input()
s = s.split(" ")
s = list(map(int, s))

d = s[0] * s[2] + 0.5 * s[1] * s[2] * s[2]
print("{:.9f}".format(d))
