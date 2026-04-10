
data = {
    1 : "a",
    2 : "b"
}
print(data[1])
text = "ram"
my_text = "hari"
text1 = ""
print(text.isalpha())
x = ("key", "key1")
y = 0
this_dict = dict.fromkeys (x,y)
print(this_dict)
data = {
    1 : "a",
    2 : "b"
}
for x in data.values():
    print(x)
for x in data.items ():
    print(x)
age = 43
if age >=10:
    print ("eligible")
else:
    print ("not eligible")
A = 23
B = 34
if B>A:
    print("B is greater than A")
A = 15
if A>0:
    print("positive")
else:
    print("negative")

def greet():
    print("hello cheers!")
greet()
def greet1(f_name):
    print("f_name, hello")
greet1("ram")
T1 = 100
C1 = (T1-32)*5/9
print(C1)

T2 =67
C2 = (T2-32)*5/9
print(C2)

def fah_to_cel(fah):
    return (fah-32)*5/9
print(fah_to_cel (35))
def myfunction(fname,lname):
    print("name:"+fname+lname)
myfunction('ram',' adhikari') 


def my_function (name):
    print("hello", name)
my_function("ram")

class student:
    name = "keshab"
    year = 2026
s1 = student()
print(s1.name)
print(s1.year)

class Person2:
    def __init__(self, name, age): # self - pointer - which we will initialize to the objects which we are referring
        self.name = name
        self.age = age
 
p3 = Person2("Nick", 19)
 
print(p3.name)
print(p3.age)