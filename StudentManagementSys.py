class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)
        print(f"{self.name} has enrolled in '{course.name}'.")

    def display_courses(self):
        print(f"{self.name}'s Enrolled Courses:")
        for course in self.courses:
            print(course.name)


class Course:
    def __init__(self, course_id, name, instructor):
        self.course_id = course_id
        self.name = name
        self.instructor = instructor


def main():
    students = []
    courses = []

    while True:
        print("==============Student Management System==============")
        print("Commands:")
        print("1. Enroll student in a course")
        print("2. Display student's enrolled courses")
        print("3. Exit")

        command = input("Enter a command: ")

        if command == "1":
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            student = Student(student_id, name)

            print("Available Courses:")
            for course in courses:
                print(f"Course ID: {course.course_id}, Name: {course.name}")

            course_id = int(input("Enter course ID to enroll in: "))
            selected_course = next((course for course in courses if course.course_id == course_id), None)
            if selected_course:
                student.enroll_course(selected_course)
            else:
                print("Invalid course ID.")

            students.append(student)

        elif command == "2":
            student_id = int(input("Enter student ID: "))
            selected_student = next((student for student in students if student.student_id == student_id), None)
            if selected_student:
                selected_student.display_courses()
            else:
                print("Student not found.")

        elif command == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid command. Please enter a valid command.")


if __name__ == "__main__":
    main()
