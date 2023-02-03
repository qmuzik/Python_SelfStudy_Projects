from decimal import *

item = Decimal( 0.70 )
rate = Decimal( 1.05 )

tax = item * rate
total = item + tax

# Displays the varibles formatted as two decimal points 
print('Item:\t','%.2f' % item)
print('Tax:\t','%.2f' % tax)
print('Total:\t','%.2f' % total)