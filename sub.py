# Storing fixed student details in a tuple
student_info = ("Alice", 10, "S101")

# Accessing tuple values
print("Student Name:", student_info[0])
print("Grade:", student_info[1])
print("Student ID:", student_info[2])

# Creating subject sets for different days
monday_subjects = {"Math", "English", "Science", "History"}
tuesday_subjects = {"Science", "Art", "Math", "PE"}

# Modifying sets
monday_subjects.add("Computer Science")
tuesday_subjects.discard("PE")

print("\nUpdated Monday Subjects:", monday_subjects)
print("Updated Tuesday Subjects:", tuesday_subjects)

# Set operations
common_subjects = monday_subjects.intersection(tuesday_subjects)
all_subjects = monday_subjects.union(tuesday_subjects)
unique_to_monday = monday_subjects.difference(tuesday_subjects)

print("\nSubjects on both days (Intersection):", common_subjects)
print("All unique subjects (Union):", all_subjects)
print("Subjects only on Monday (Difference):", unique_to_monday)