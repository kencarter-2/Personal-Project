print("== Grade Calculator ==")

student_name = input("Enter student name: ")
course_name = input("Enter course name: ")

test1 = float(input("Enter Test 1 grade: "))
test2 = float(input("Enter Test 2 grade: "))
test3 = float(input("Enter Test 3 grade: "))

homework = float(input("Enter homework average: "))
quiz = float(input("Enter quiz average: "))

test_average = (test1 + test2 + test3) / 3

final_average = (test_average + homework + quiz) / 3

print()
print("=== Grade Report ===")
print("Student:", student_name)
print("Course:", course_name)
print("Test average:", test_average)
print("Homework average:", homework)
print("Quiz average:", quiz)
print("Final average:", final_average)
