n = int(input())
while n != 0:
    food = set()
    food_dict = {}
    for i in range(n):
        temp = input()
        temp = temp.split(' ')
        for j in range(1, len(temp)):
            if(temp[j] in food_dict):
                food_dict[temp[j]] = food_dict[temp[j]] + " "+ temp[0]
            else:
                food_dict[temp[j]] = temp[0]
                food.add(temp[j])
    food = list(food)
    food.sort()
    for f in food:
        name = food_dict[f].split(' ')
        name.sort()
        name = ' '.join(name)
        print(f, name)
    n = int(input())
    
