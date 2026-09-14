s={"apple","banana","grapes","kiwi","watermelon"}
print(s)
print(len(s))
s.add("orange")
print(s)
s1={"red","white","black","blue"}
s.update(s1)
print(s1)
s.remove("apple")
print(s)
s1.discard("red")
s.pop()


numbers = {10, 20, 30, 40, 50}

number = int(input("Enter a number: "))

if number in numbers:
    print("Number exists in the set")
else:
    print("Number does not exist")


set1={1,2,3}
set2={3,4,5}
result=set1.union(set2)
result=set1.intersection(set2)
result=set1.difference(set2)
result=set1.symmetric_difference(set2)
print("union:",result)
print("intersetion:",result)
print("difference:",result)
print("symmertic_difference:",result)

set3 = {1, 2}
set4 = {1, 2, 3, 4}

if set3.issubset(set4):
    print("Set3 is a subset of Set4")
else:
    print("Set3 is not a subset of Set4")



set5 = {1, 2, 3, 4}
set6 = {1, 2}

if set1.issuperset(set5):
    print("Set5 is a superset of Set6")
else:
    print("Set5 is not a superset of Set6")   


numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = set(numbers)

print("Original list:", numbers)
print("Set without duplicates:", unique_numbers)    