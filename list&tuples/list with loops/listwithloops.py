#program to check whether the number is even
num=[1,2,3,4,5,6,7,8,9]
for i in num:
    if(i%2==0):
        print("is even",i)

#program to check whether the number is odd
num=[1,2,3,4,5,6,7,8,9]
for i in num:
    if(i%2!=0):
        print("is odd",i)        
#program 3
list1=[1,2,3,4,5,6,7,8,9]        
print(max(list1))
print(min(list1))
print(sum(list1)/len(list1))

#number of elements greater than 50
numbers = [20, 60, 45, 80, 30, 90, 55]

count = 0

for num in numbers:
    if num > 50:
        count = count + 1

print("Numbers greater than 50:", count)


#program to separate even and odd numbers from a list
numbers = [10, 15, 20, 25, 30, 35]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)


#program to remove duplicates from a list
numbers = [10, 20, 10, 30, 20, 40, 30]

new_list = []

for num in numbers:
    if num not in new_list:
        new_list.append(num)

print("Original list:", numbers)
print("List without duplicates:", new_list)


#program to calculate squares of numbers in a list
numbers = [1, 2, 3, 4, 5]

squares = []

for num in numbers:
    squares.append(num * num)

print("Numbers:", numbers)
print("Squares:", squares)