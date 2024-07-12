n = int(input())
s = input()
for i in range(n):
    if not s[i].isdigit():
        s = s.replace(s[i]," ")
nums = s.split(" ")
arr = []
for j in range(len(nums)):
    if nums[j] != '':
        arr.append(int(nums[j]))
print(max(arr))
