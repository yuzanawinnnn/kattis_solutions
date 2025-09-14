while True:
    s = list(map(int, input().split(" ")))
    if(s[0] > s[1]):
        print("More")
    elif(s[0] < s[1]):
        print("Less")
    else:
        break
