bunny = [1,1+1,3,2,3]
print(bunny)

doggy = [[1,1+1,4-1],{2*2,5,6}, "yo"]
print(doggy)


print(sum([1,1,0,1,0,1,0]))
print(sum([1,1,0,1,0,1,0], -9))

print(sum([ [1,2,3], [4,5,6], [7,8,9] ],[]))

cartesian = [ [x,y] for x in ['A','B','C'] for y in [1,2,3]]
print(cartesian)

# slices that skip

L = [0,10,20,30,40,50,60,70,80,90]
print(L[:5])
print(L[5:])
print(L[::2])
print(L[1::2])

