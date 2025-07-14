names = [ "Abdul", "Abrar", "Farhan", "Affan", "Aamir"]
print(names)
print(names[0])
print(names[3])
print(names[1])
print(names[-1])
print(names[-3])
names[0]="Abdullah"
print(names[0])
print(names[0:4])


numbers= [1, 2, 3, 4, 5]
numbers.append(6)
numbers.append(7)
numbers.insert(0, -1)
numbers.insert(8, 8)
numbers.remove(2)
print(numbers)
print(5 in numbers)
print(len(numbers))
numbers.clear()
print(numbers)