s = input()
full = ["U", "A", "P", "C"]
ans = ""

for i in range(len(full)):
    if full[i] not in s:
        ans = ans + full[i]

print(ans)
