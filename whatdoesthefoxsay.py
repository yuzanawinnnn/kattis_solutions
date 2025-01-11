n = int(input())
for j in range(n):
    all_sound = input() #the sound of all animals
    all_sound = all_sound.split(" ")
    animal_sound = [] #the list of the sound of each animal
    s = ""
    animals = input()
    while True:
        if(animals == "what does the fox say?"):
            break
        animals  = animals.split(" ")
        animal_sound.append(animals[animals.index("goes") + 1])
        animals = input()
    for i in range(len(all_sound)):
        if(all_sound[i] not in animal_sound):
            s = s + all_sound[i]+ " "
    print(s[:len(s)-1])
        
