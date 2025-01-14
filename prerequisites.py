while True:
    flag = input() #no. of course, categories
    if(flag == "0"):
        break
    flag = flag.split(" ")
    courses = input()
    courses = courses.split(" ")
    yn = True
    for i in range(int(flag[1])):
        categ = input()
        count = 0
        categ = categ.split(" ")
        for j in range(2,len(categ)):
            if(categ[j] in courses):
                count = count + 1
        if yn == True and count < int(categ[1]):
            yn = False
    if(yn == True):
        print("yes")
    else:
        print("no")
    
