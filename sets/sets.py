S = {1,2,3}
print('S = ',S)
print('2 in S=',2 in S)

# union
print('Union of {1,2,3} and {2,3,4,5,6}:')
union = {1,2,3} | {2,3,4,5,6}
print(union,'\n')

# intersection
print('intersection of {1,2,3} and {2,3,4,5,6}:')
intersection = {1,2,3} & {2,3,4,5,6}
print(intersection,'\n')

# add
print('added 4 to S:')
S.add(4)
print(S,'\n')

Friends = {'Sair','Sagar','Liaqat','Azhar'}
print(Friends)
print('added ali to Friends:')
Friends.add('Ali')
print(Friends,'\n')

# remove
print('remove 4 to S:')
S.remove(4)
print(S,'\n')

print('removed sagar from Friends:')
Friends.remove('Sagar')
print(Friends,'\n')


#update
print('update {7,8,9} to S')
S.update({7,8,9})
print(S,'\n')

#intersection_update
print('intersection_update {3,7,11,20} to S')
S.intersection_update({3,7,11,20})
print(S,'\n')


# bound variables
print('T=S,T.remove,T=')
T=S
T.remove(7)
print(S,'\n')


# copy 
# The assignment statement binds U not to the value of S but to a copy of that value,
print('U=S.copy(), add 0 to U' )
U=S.copy()
U.add(0)
print('S=',S,'\n')
print('U=',U,'\n')

