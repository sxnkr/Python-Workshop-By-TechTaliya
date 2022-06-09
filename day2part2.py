'''Python tuple'''

#Python tuple is used to store the sequence in a immutable form.
tuple1=(1,2,3,4,5,6,7)
#We can use indexing and splitting operaton

#Tuple op
# same as list


'''Python set'''

#The set in python can be defined as the unorderd collection of various items enclosed within the curly braces.

s={5,563,4,6,35,2}
#Adding an element
s.add(23)
#in discard we dont get a error if the element asked to be removed id not present
s.discard(6)
print(s)
#But in remove we get an error.
s.remove(563)
print(s)
#Removing the first element in the set.
s.pop()
print(s)

s1={"i","am"}
s2={"an","Indian"}
#union of two set
#here we are combing the two set and printing the output.
print(s1|s2)
print(s1.union(s2))
print(s1)
S1={"I","love","my","country"}
S2={"India","is","my","country"}
print(S1&S2)
print(S1.intersection(S2))


'''Frozen sets'''

#immutable sets

set2=frozenset([1,23,45,6,34])
print(type(set2))
