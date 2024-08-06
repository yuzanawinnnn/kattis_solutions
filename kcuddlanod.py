n = input()
bags = n.split(" ")
if(len(bags[0]) > len(bags[1])):
    print(1)
elif(len(bags[0]) < len(bags[1])):
   print(2) 
else:
    first = bags[0][::-1]
    second = bags[1][::-1]

    if('5' in first):
        first = first.replace('5', '!')
    if('2' in first):
        first = first.replace('2', '5')
    if('!' in first):
        first = first.replace('!', '2')
    if('5' in second):
        second = second.replace('5', '!')
    if('2' in second):
        second = second.replace('2', '5')
    if('!' in second):
        second = second.replace('!', '2')

    for i in range(len(first)):
        if(int(first[i]) > int(second[i])):
            print(1)
            break
        elif(int(first[i]) < int(second[i])):
            print(2)
            break
