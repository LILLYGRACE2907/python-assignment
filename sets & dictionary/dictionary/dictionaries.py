student={
    "name":"lilly",
    "age":18,
    "course":"CCN",
}
print(student)
#Access a Value Using Its Key
print("name:",student["name"])
print("age:",student["age"])
#Add a New Key-Value Pair
student["marks"]=830
print(student)
#Update an Existing Value
student["name"]="grace"
print(student)
#Remove Key-Value Pair Using pop()
student.pop("marks")
print(student)
#Remove Last Inserted Item Using popitem()
student.popitem()
print(student)
#rint All Keys Using keys()
print(student.keys())
#print All Keys Using values()
print(student.values())
#print All Key-Value Pairs Using items()
print(student.items())
print("name" in 'students')