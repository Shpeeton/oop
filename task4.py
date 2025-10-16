class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return "Ошибка"

        if course not in self.courses_in_progress:
            return "Ошибка"

        if course not in lecturer.courses_attached:
            return "Ошибка"

        if grade < 0 or grade > 10:
            return "Ошибка"

        if course not in lecturer.grades:
            lecturer.grades[course] = []
        lecturer.grades[course].append(grade)
        return None

    def average_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        avg_grade = self.average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        avg_grade = self.average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def calculate_average_student_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])

    if not total_grades:
        return 0
    return sum(total_grades) / len(total_grades)


def calculate_average_lecture_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])

    if not total_grades:
        return 0
    return sum(total_grades) / len(total_grades)

lecturer = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Мария', 'Козлова')
reviewer = Reviewer('Пётр', 'Петров')
reviewer2 = Reviewer('Артём', 'Канищев')
student = Student('Ольга', 'Васина', 'Ж')
student2 = Student('Алексей', 'Журавлев', 'М')

student.courses_in_progress += ['Python', 'Java']
student.finished_courses += ['Введение в программирование']
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Git']
lecturer.courses_attached += ['Python', 'C++']
lecturer2.courses_attached += ['Python']
reviewer.courses_attached += ['Python', 'C++']
reviewer2.courses_attached += ['Git']
student.grades = {'Python': [8, 9, 7]}
student2.grades = {'Python': [9, 8, 9]}

print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecture(lecturer, 'C++', 8))  # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка
print(student2.rate_lecture(lecturer2, 'Python', 9))  # None
print(student2.rate_lecture(lecturer2, 'Python', 10))  # None

print(lecturer.grades)  # {'Python': [7]}
print(lecturer2.grades)  # {'Python': [9, 10]}

print(lecturer)
print(lecturer2)
print(reviewer)
print(reviewer2)
print(student)
print(student2)

print(lecturer == lecturer2)  # False
print(student == student2)  # False

print("СРЕДНИЕ ОЦЕНКИ:")
students_list = [student, student2]
lecturers_list = [lecturer, lecturer2]

course_name = 'Python'
avg_student_grade = calculate_average_student_grade(students_list, course_name)
avg_lecture_grade = calculate_average_lecture_grade(lecturers_list, course_name)

print(f"Средняя оценка за домашние задания по курсу '{course_name}': {avg_student_grade:.1f}")
print(f"Средняя оценка за лекции по курсу '{course_name}': {avg_lecture_grade:.1f}")