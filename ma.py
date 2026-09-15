# List  -  ordered, can be changed
scores = [79, 96, 83, 85]

# Dictionary  -  labelled key-value pairs
student = {"name": "Dave", "age": 13}

coordinates = (10, 20)


colours = {"red", "blue", "green"}

fruits = ["apple", "mango", "banana", "grapes", "orange"]

print(fruits[0])    
print(fruits[-1])    

print(len(fruits))   # 5

print(fruits[1:3])   
fruits = ["apple", "mango", "banana", "grapes"]

fruits.append("orange")   # Add to end

fruits.remove("mango")    # Remove by value


fruits.pop(1)             # Remove by index  (removes 'banana')

fruits.sort()             # Sort alphabetically

fruits.reverse()          # Reverse the order


fruits.clear()            # Remove all items

student = {"name": "Javys", "age": 16, "grade": 12}

# Accessing values by key
print(student["name"])    
print(student["age"])    

print(student)


student = {"name": "John", "age": 14, "grade": 9}


print(student.get("age"))              
print(student.get("school", "N/A"))     

student["age"] = 14

student["school"] = "Lakeside High"
print(student)


student.pop("grade")
print(student)

student.clear()
print(student)   # {}


roll_numbers = [1, 2, 3, 4, 5]
names = ["John", "Alice", "Rahul", "Maria", "David"]

# Convert to a dictionary using zip()
students = dict(zip(roll_numbers, names))
print(students)

# Look up a student by roll number
print(students[3])   # Rahul
