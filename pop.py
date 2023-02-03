basket = [ 'Apple', 'Bun', 'Cola' ] # Basket list and string values
crate = [ 'Egg', 'Fig', 'Grape' ] # Crate list and string values 

print( 'Basket List:' , basket ) # Display the basket element list's 
print( 'Basket Elements:' , len( basket ))

basket.append( 'Damson' ) # Adds element, display all list elements, removes the final element and displays all elements
print( 'Appended:' , basket )
print( 'Last Item Removed:' , basket.pop() )
print( 'Basket List:' , basket )

basket.extend( crate ) # Adds statements to elemtns from second list to the first list, removes them and displays
print( 'Extended:' , basket )
del basket[1]
print( 'Item Removed:' , basket )
del basket[1:3]
print( 'Slice Removed:' , basket )


