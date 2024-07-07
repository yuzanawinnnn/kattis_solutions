nums = input()
nums = nums.split(" ")
count = 0
for i in range(int(nums[0])):
    temp = input()
    crayon = temp.split(" ")
    crayon = list(dict.fromkeys(crayon))
    count = count + (int(nums[1]) - len(crayon))
print(count)
