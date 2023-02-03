from time import *

# Initializes start_timer varible 
start_timer = time()

# Creates an start_timer object 
struct = localtime(start_timer)

# Annouces the countdown from the starting point
print('\nStarting Countdown At:', strftime('%X',struct))

# Loop to print counter varible and decrements it by one 
i = 10
while i > -1:
    print(i)
    i -= 1
    sleep(1)

# Initializes end_timer varible
end_timer = time()

# Initializes difference varible with rounded seconds value between the two timed points
difference = round(end_timer - start_timer)

# Displays the time taken execute loop
print('\nRuntime:',difference,'Seconds')