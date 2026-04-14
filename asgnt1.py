#ans1. Explain the difference between List and Tuple.

#List items are ordered, changeable, and allow duplicate values and uses []
#Tuple items are ordered, unchangeable, and allow duplicate values and uses ().

#Create a list
my_list = [10, 20, 30, 40]
print(my_list)
#Convert it into a tuple
my_tuple = tuple(my_list)
print(my_tuple)
#Try modifying both
my_list[0] = 15
print(my_list)
#my_tuple[0] = 15
print(my_tuple)

#ans2. A set is a collection which is unordered, unchangeable but can remove items and add new items,duplicate not allowed and unindexed and uses {}.
#Sets are data structures that inherently store unique elements, when an item is added to a set, it checks for existing duplicates If the item already exists, it is not added again.
#Write a program to remove duplicates from a list and print unique values.
my_list1 = [1,1,2,2,3,4,5]
unique_number = list(set(my_list1))
print(unique_number)

#ans3. Reverse a list using slicing
my_list3 = [1,2,3,4,5]
reverse_list = my_list3 [::-1]
print(reverse_list)
#Also print original list to show it is unchanged
print(my_list3)

#ans4. Create a dictionary of student details
students = {
    "name": "keshab",
    "age" : 35,
    "grade": "A"
}
#Access the name
print(students["name"])
#Remove age using pop()
print(students.pop("age"))
print(students)
#Print length of dictionary
print(len(students))

#ans.5 Take a string
#Check if it contains only alphabets
#Print "Valid" or "Invalid"
print("keshab".isalpha()) 
print("keshab1".isalpha()) 