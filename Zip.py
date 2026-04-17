students = ["ram", "hari", "shyam"]
scores = [10, 20,30]
for name, score in zip(students, scores):
    print(score,name)

set = {1,2,3,4,5,5}
print(set)
set.add (6)
print(set)
# That insert new element in the set
set.add (3)
print(set)
# That if value exist already and you try to added it simply get ignored/no duplicate added.


set.remove (2)
print(set)
# Removes deletes specific element from the set.

set.remove (8)
print(set)
# If you try to remove the any number not present on set it give keyerror.
set.discard (10)
print(set)
# Using discard you will get no keyerror 
A = {1,2,3}
B = {3,4,5}
print (A & B)
pages = [1,2,3,4,5]
my_pages = set(pages)
print (my_pages)
