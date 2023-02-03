from datetime import *

# Creates datetime object and displays its contents
today = datetime.today()
print('Today is:',today)

# Loop to display each value individually 
for attr in \
    ['year','month','day','hour','minute','second','microsecond']:
    print(attr,':\t',getattr(today,attr))

# Display time in dot notation
print('Time: ',today.hour,':',today.minute,sep = '')

# Assigns formatted day and month to varibles 
day = today.strftime('%A')
month = today.strftime('%B')

# Displays the formatted date 
print('Date:',day,month,today.day)
