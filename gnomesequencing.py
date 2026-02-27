n = int(input())
print("Gnomes:")
for i in range(n):
    s = input()
    s = s.split(" ")
    s = list(map(int, s))
    sorted_list = sorted(s)
    rev_sorted_list = sorted(s, reverse = True)
    if(s == sorted_list or s == rev_sorted_list):
        print("Ordered")
    else:
        print("Unordered")
