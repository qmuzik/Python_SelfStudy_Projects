a = 2
b = 4
c = 8

print( '\nDefault Order:\t', a, '*', c, '+', b, '=', a * c + b) # Forces addition before subtraction 
print( 'Forced Order:\t', a, '* (', c, '+', b, ') =', a * (c + b))

print( '\nDefault Order:\t', c, '//', b, '-', a, '=', c // b - a) # Forces subtraction before division 
print( 'Forced Order:\t', c, '// (', b, '-', a, ') =', c // ( b - a))

print( '\nDefault Order:\t', c, '%', a, '+', b, '=', c % a + b) # Forces addition before modulo operation 
print( 'Forced Order:\t', c, '% (', a, '+', b,') =', c % ( a + b))

print( '\nDefault Order:\t', c, '**', a, '+', b, '=', c ** a + b) # Forces addition before exponent operation
print( 'Forced Order:\t', c, '** (', a, '+', b, ') =', c ** ( a + b )) 