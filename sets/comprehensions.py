# comprehension
comp = {x**2 for x in {1,2,3}}
print(comp)


comp = {2*x for x in {'A','B'}}
print(comp)


# union
S= {3,5,7}
comp = {x**2 for x in S|{1,2,3}}
print(comp)

#intersection
comp = {x**2 for x in S&{1,2,3}}
print(comp)

#filter
comp = {x**2 for x in {1,2,3} if x>2}
print(comp)


# double comprehension
comp = {x*y for x in {1,2,3} for y in {2,3,4}}
print(comp)


comp = {x*y for x in {1,2,3} for y in {2,3,4} if x != y}

print(comp)