#accessing elements in a list
marks = [80, 90, 75, 85]

print(marks[0])
print(marks[1])
print(marks[3])


#accessing elements in a list
marks = [80 , 90 , 75 , 85]

print(marks[0])
print(marks[1])
print(marks[3])


#add elements to a list
marks = [80, 90, 75]

marks.append(85)

print(marks)

marks = [55, 80, 45]
marks.append(60)
print(marks)


#remove elements from a list
marks = [80, 90, 75]

marks.remove(90)
print(marks)


#insert
numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)


#extend
a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)
print(a)


#clear
numbers = [10, 20, 30]

numbers.clear()

print(numbers)


#index
numbers = [10, 20, 30, 40]
print(numbers.index(30))


#count
numbers = [10, 20, 20, 30, 20]

print(numbers.count(20))


#sort elements
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

numbers.sort(reverse = True)

print(numbers)


#copy
a = [1, 2, 3]

b = a.copy()

print(b)


#
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3]) 
print(numbers[2:5])
print(numbers[::-1])
print(numbers[-4::])
print(numbers[-1::])
print(numbers[::-2])