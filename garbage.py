from Songbird import*

# Creates an instance of the class
bird_1 = Songbird('Koko','Tweet, tweet!\n')
print(bird_1.name,'ID:',id(bird_1))
bird_1.sing()

# Deletes instance of the class 
del bird_1

# Creates two new instance of the class
bird_2 = Songbird('Louie','Chirp, chirp!\n')
print(bird_2.name,'ID:',id(bird_2))
bird_2.sing()

bird_3 = Songbird('Misty','Squawk, squawk!\n')
print(bird_3.name,'ID:',id(bird_3))
bird_3.sing()

# Deletes instances of class
del bird_2
del bird_3