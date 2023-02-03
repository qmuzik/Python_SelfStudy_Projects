import math , random

# Rounds 9.5 either up or down 
print('Rounded Up 9.5:', math.ceil(9.5))
print('Rounded Down 9.5:', math.floor(9.5))

# Initializes a varible of 4
num = 4

# Calculates sqaure and sqaure root
print(num,'Sqaured:', math.pow( num , 2))
print(num, 'Sqaure Root:',math.sqrt(num))

# Produces random list of six numbers between 1 and 59
nums = random.sample(range(1,59),6)

# Displays the random list
print('Your Lucky Lotto Numbers Are:', nums)