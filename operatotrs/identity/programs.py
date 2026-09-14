class Person:
	pass


# Two variables referencing the same list.
first_list = [1, 2, 3]
second_list = first_list
print("Same list with is:", first_list is second_list)

# Two separate lists can have the same values but different identities.
list_a = [1, 2, 3]
list_b = [1, 2, 3]
print("Separate lists with ==:", list_a == list_b)
print("Separate lists with is:", list_a is list_b)
print("Difference between == and is:", list_a == list_b and list_a is not list_b)

# Two variables referencing the same object, checked with is not.
shared_object = {"language": "Python"}
object_alias = shared_object
print("Same object with is not:", shared_object is not object_alias)

# Two dictionaries with the same data are equal, but are not identical.
dictionary_a = {"name": "Ada", "age": 36}
dictionary_b = {"name": "Ada", "age": 36}
print("Dictionaries have the same data:", dictionary_a == dictionary_b)
print("Dictionaries have the same identity:", dictionary_a is dictionary_b)

# Build tuples separately so their identities are compared explicitly.
tuple_a = tuple(["red", "green", "blue"])
tuple_b = tuple(["red", "green", "blue"])
print("Tuples have the same identity:", tuple_a is tuple_b)

# None should be checked with is None and is not None.
empty_value = None
print("Value is None:", empty_value is None)

defined_value = "available"
print("Value is not None:", defined_value is not None)

# Two objects of the same class are different objects.
person_a = Person()
person_b = Person()
print("Same class:", type(person_a) is type(person_b))
print("Same object:", person_a is person_b)

# Custom class objects demonstrate == versus is.
person_alias = person_a
print("Custom objects with ==:", person_a == person_alias)
print("Custom objects with is:", person_a is person_alias)
