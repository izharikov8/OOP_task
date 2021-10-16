class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade): # Задание 2.
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total = []
        qty = []
        for key, value in self.grades.items():
            total_grades = sum(value)
            qty_grades = len(value)
            total.append(total_grades)
            qty.append(qty_grades)
        res = (sum(total) / sum(qty))
        return round(res, 2)

    def __str__(self): # Задание 3.
        res = f'Имя: {self.name}\n'
        res += f'Фамилия: {self.surname}\n'
        res += f'Средняя оценка за домашние задания: {Student.average_grade(self)}\n'
        res += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        res += f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def __lt__(self, other): # Задание 3.
        if not isinstance(other, Student):
            print('Такого студента нет!')
            return
        return Student.average_grade(self) < Student.average_grade(other)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def __str__(self): # Задание 3.
        res = f'Имя: {self.name}\n'
        res += f'Фамилия: {self.surname}'
        return res


class Lecturer(Mentor): # Задание 1.
    def __str__(self):
        res = f'Имя: {self.name}\n'
        res += f'Фамилия: {self.surname}\n'
        res += f'Средняя оценка за лекции: {Student.average_grade(self)}'
        return res

    def __lt__(self, other): # Задание 3.
        if not isinstance(other, Lecturer):
            print('Такого лектора нет!')
            return
        return Student.average_grade(self) < Student.average_grade(other)


class Reviewer(Lecturer): # Задание 1.
    def __str__(self): # Задание 3.
        res = f'Имя: {self.name}\n'
        res += f'Фамилия: {self.surname}'
        return res

    def rate_hw(self, student, course, grade): # Задание 2.
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Задание 4.
best_student = Student('Wendy', 'Testaburger', 'female')
bad_student = Student('Eric', 'Cartman', 'male')
cool_mentor = Mentor('Randy', 'Marsh')
bad_mentor = Mentor('PC', 'Principal')
cool_lecturer = Lecturer('Stan', 'Marsh')
bad_lecturer = Lecturer('Butters', 'Stotch')
cool_reviewer = Reviewer('Kenny', 'McKormik')
bad_reviewer = Reviewer('Kyle', 'Broflovski')

best_student.courses_in_progress += ['Python', 'Java']
bad_student.courses_in_progress += ['Python', 'Java']
cool_mentor.courses_attached += ['Python', 'Java']
cool_lecturer.courses_attached += ['Java', 'Python']
cool_reviewer.courses_attached += ['Python', 'Java']
bad_lecturer.courses_attached += ['Java', 'Python']
bad_reviewer.courses_attached += ['Python', 'Java']
best_student.finished_courses += ['Введение в программирование']
bad_student.finished_courses += ['Введение в программирование']

best_student.rate_lecturer(bad_lecturer, 'Python', 3)
best_student.rate_lecturer(bad_lecturer, 'Java', 4)
bad_student.rate_lecturer(bad_lecturer, 'Java', 5)
best_student.rate_lecturer(cool_lecturer, 'Python', 8)
best_student.rate_lecturer(cool_lecturer, 'Java', 8)
bad_student.rate_lecturer(cool_lecturer, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Java', 10)
cool_reviewer.rate_hw(bad_student, 'Python', 3)
bad_reviewer.rate_hw(bad_student, 'Java', 4)


lecturers_list = [cool_lecturer, bad_lecturer]
students_list = [best_student, bad_student]


def hw_average(data, course):
    total = []
    for el in data:
        total.append(sum(el.grades[course]) / len(el.grades[course]))
    print(f'Средняя оценка студентов по курсу {course}: {sum(total) / len(total)}')


def lecture_average(data, course):
    total = []
    for el in data:
        total.append(sum(el.grades[course]) / len(el.grades[course]))
    print(f'Средняя оценка лекторов по курсу {course}: {sum(total) / len(total)}')


print(best_student)
print(bad_student)
print(cool_mentor)
print()
print(cool_lecturer)
print()
print(cool_reviewer)
print()
print(best_student < bad_student)
print()
print(cool_lecturer > bad_lecturer)
print()
lecture_average(lecturers_list, 'Python')
lecture_average(lecturers_list, 'Java')
hw_average(students_list, 'Java')
hw_average(students_list, 'Python')