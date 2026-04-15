salary = 12000
if salary>1000:
    print("high salary")
elif salary >=5000:
    print("medium salary")
else:
    print("low salary")

salaries = [10000, None, 5000, 2000, None]
for s in salaries:
    if s is not None:
        print(s)

salary3 = [10000,20000,3000]
for x in salary3:
    bonus = x*.10
    print(bonus)

numbers = [1, 2, 3, 4, 5]

for n in numbers:
    if n % 2 == 0:
        print(n, "Even")
    else:
        print(n, "Odd")


marks = [90, 40, 75, 30]
for m in marks:
    if m >= 50:
        print(m, "Pass")
    else:
        print(m, "Fail")

def add_bonus (salaries):
    bonus = salaries*.10
    total_salary = salaries+bonus
    return total_salary

salary4 = [1000,2000,3000]
for i in salary4:
    result = add_bonus(i)
    print(result)

sal=[10000,20000,25000,30000]
def add_bonus(y):
    return y+0.10*y
result1=map(add_bonus,sal)
print(list(result1))

numbers = [1,2,3]
result = map(lambda x: x+10,numbers)
print(list(result))

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp = Employee("keshab", 10000)

print(emp.name)
print(emp.salary)

class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)   # call parent constructor
        self.salary = salary


emp = Employee("arbin", 2000)
emp.show_name()
        