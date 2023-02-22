def input_student_data():
    num_students = int(input("Enter the number of students: "))
    students = []
    for i in range(num_students):
        name = input("Enter student name: ")
        marks = []
        for j in range(3):
            mark = int(input(f"Enter mark {j+1}: "))
            marks.append(mark)
        student = (name, marks)
        students.append(student)
    return students

def display_student_data(students):
    for student in students:
        name, marks = student
        print(f"Name: {name}")
        print("Marks: ")
        for i, mark in enumerate(marks):
            print(f"  Mark {i+1}: {mark}")
        print()

def calculate_student_avg(students):
    student_avgs = {}
    for student in students:
        name, marks = student
        avg = sum(marks) / len(marks)
        student_avgs[name] = avg
    return student_avgs

def display_student_avg(student_avgs):
    for name, avg in student_avgs.items():
        print(f"{name} average mark: {avg:.2f}")

def run():
    students = input_student_data()
    display_student_data(students)
    student_avgs = calculate_student_avg(students)
    display_student_avg(student_avgs)

if __name__ == "__main__":
    run()
