#lambda params: expr(params)
val=5
x=2
y=3
def double(val):
    return  val*2
double(5)
lambda val: val*2
lambda x,y:x+y
p='good'
lambda p:p[0]+p[1]
(lambda x: x > 3)(4)  # => True

# Squares from 0**2 to 9**2
map(lambda val: val ** 2, range(10))

# Tuples with positive second elements
filter(lambda pair: pair[1] > 0, [(4,1), (3, -2), (8,0)])

# Sort a collection based on a custom function.
sorted([(4,1), (3, -2), (8,0)], key=lambda pair: pair[1])