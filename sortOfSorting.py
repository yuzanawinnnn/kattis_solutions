while True:
    n = int(input())
    if(n == 0):
        break
    arr = []
    for i in range(n):
        name = input()
        arr.append(name)
    arr.sort(key=lambda x: x[:2])
    for j in range(n):
        print(arr[j])
    print("")
