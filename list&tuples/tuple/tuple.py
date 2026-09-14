t=("red","blue","green","yellow","black")
print(t)
print(t[0])
print(t[4])
print(t[0:4])

l=(1,2,3,4,5,3,4,4,4,4,4,4,4,4,)
print(l.count(4))
print(l.index(3))
print(l.index(2))
print(l.index(4,5,10))

#largest or smallest
y=(1,2,3,4,5,6,7,8,9)
largest = max(y)
smallest = min(y)

print("Largest:", largest)
print("Smallest:", smallest)

#access each element individually
student = ("Lilly", 18, "CCN", 85)

print("Name:", student[0])
print("Age:", student[1])
print("Course:", student[2])
print("Marks:", student[3])

#unpacking
student = ("Lilly", 18, "CCN", 85)

name, age, course, marks = student

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("Marks:", marks)

#swapping
a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)