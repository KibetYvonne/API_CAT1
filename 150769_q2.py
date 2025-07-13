class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment_grade(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Grade {grade} added for '{assignment_name}' to student {self.name}.")

    def display_grades(self):
        print(f"\nGrades for {self.name}:")
        if not self.assignments:
            print("  No assignments yet.")
        for assignment, grade in self.assignments.items():
            print(f"  {assignment}: {grade}")

    def __str__(self):
        return f"{self.name} (ID: {self.student_id})"


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added to course '{self.course_name}'.")

    def assign_grade_to_student(self, student_id, assignment_name, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment_grade(assignment_name, grade)
                return
        print(f"Student ID {student_id} not found.")

    def display_all_students_and_grades(self):
        print(f"\nAll students and their grades in '{self.course_name}':")
        if not self.students:
            print("  No students enrolled.")
        for student in self.students:
            student.display_grades()


def main():
    instructor_name = input("Enter instructor's name: ")
    course_name = input("Enter course name: ")
    instructor = Instructor(instructor_name, course_name)

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Assign Grade to Student")
        print("3. Display All Students and Grades")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)

        elif choice == '2':
            student_id = input("Enter student ID: ")
            assignment = input("Enter assignment name: ")
            try:
                grade = float(input("Enter grade: "))
                instructor.assign_grade_to_student(student_id, assignment, grade)
            except ValueError:
                print("Invalid grade. Must be a number.")

        elif choice == '3':
            instructor.display_all_students_and_grades()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
 