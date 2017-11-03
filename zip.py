#range
aList = list(range(10))
print(aList)

#zip
print(list(zip([1,3,5],[2,4,6])))

characters = ['Neo', 'Morpheus', 'Trinity']
actors = ['Keanu', 'Laurence', 'Carrie-Anne']
set(zip(characters, actors))
print([character+' is played by '+actor for (character,actor) in zip(characters,actors)])

# reversed
print([x*x for x in reversed([4, 5, 10])])