class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\n'\
               f'Фамилия: {self.surname}\n'\
               f'Средняя оценка за лекции: {self.avr_grade()}\n'\
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'\
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Сравнение возможно только с другим студентом!'
        return self.avr_grade() == other.avr_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            return 'Сравнение возможно только с другим студентом!'
        return self.avr_grade() != other.avr_grade()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Сравнение возможно только с другим студентом!'
        return self.avr_grade() < other.avr_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Сравнение возможно только с другим студентом!'
        return self.avr_grade() > other.avr_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return 'Сравнение возможно только с другим студентом!'
        return self.avr_grade() <= other.avr_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return 'Сравнение возможно только с другим студентом!'
        return self.avr_grade() >= other.avr_grade()

    def avr_grade(self):
        all_grades = []
        for grade in self.grades.values():
            all_grades += grade
        if sum(all_grades) != 0:
            return round(sum(all_grades) / len(all_grades), 1)
        else:
            return 'Оценки отсутствуют!'

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.avr_grade()}'

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Сравнение возможно только с другим преподавателем!'
        return self.avr_grade() == other.avr_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            return 'Сравнение возможно только с другим преподавателем!'
        return self.avr_grade() != other.avr_grade()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Сравнение возможно только с другим преподавателем!'
        return self.avr_grade() < other.avr_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Сравнение возможно только с другим преподавателем!'
        return self.avr_grade() > other.avr_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return 'Сравнение возможно только с другим преподавателем!'
        return self.avr_grade() <= other.avr_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return 'Сравнение возможно только с другим преподавателем!'
        return self.avr_grade() >= other.avr_grade()

    def avr_grade(self):
        all_grades = []
        for grade in self.grades.values():
            all_grades += grade
        if sum(all_grades) != 0:
            return round(sum(all_grades) / len(all_grades), 1)
        else:
            return 'Оценки отсутствуют!'


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def students_avr_grade(students, course):
    all_grades = []
    for student in students:
        if course in student.courses_in_progress and student.grades.get(course) is not None:
            all_grades += student.grades.get(course)

    if sum(all_grades) != 0:
        print(round(sum(all_grades) / len(all_grades), 1))
    else:
        print('Оценки отсутствуют!')


def lecturers_avr_grade(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.courses_attached and lecturer.grades.get(course) is not None:
            all_grades += lecturer.grades.get(course)

    if sum(all_grades) != 0:
        print(round(sum(all_grades) / len(all_grades), 1))
    else:
        print('Оценки отсутствуют!')


# Data
student_1 = Student('Barrett', 'Syd', 'male')
student_1.courses_in_progress += ['Python', 'Java']
student_1.finished_courses += ['Git']

student_2 = Student('Floyd', 'Pink', 'male')
student_2.courses_in_progress += ['Python', 'Java']
student_2.finished_courses += ['Design']

lecturer_1 = Lecturer('Waters', 'Rogers')
lecturer_1.courses_attached += ['Python', 'Java']

lecturer_2 = Lecturer('Wright', 'Richard')
lecturer_2.courses_attached += ['Java']

reviewer_1 = Reviewer('Axel', 'David')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Shepard', 'Commander')
reviewer_2.courses_attached += ['Java']

all_students = [student_1, student_2]
all_lecturers = [lecturer_1, lecturer_2]


# Grades
student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Java', 7)
student_1.rate_lecture(lecturer_2, 'Java', 5)

student_2.rate_lecture(lecturer_1, 'Python', 6)
student_2.rate_lecture(lecturer_2, 'Java', 8)
student_2.rate_lecture(lecturer_2, 'Java', 9)


reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 7)

reviewer_2.rate_hw(student_1, 'Java', 7)
reviewer_2.rate_hw(student_2, 'Java', 8)
reviewer_2.rate_hw(student_2, 'Java', 10)


# Test
print('Эксперт:')
print(reviewer_1)
print('\nЛектор:')
print(lecturer_2)
print('\nСтудент:')
print(student_1)

print('\nСравнение student_1 и student_2 по средней оценке:')
print('==')
print(student_1 == student_2)
print('!=')
print(student_1 != student_2)
print('<')
print(student_1 < student_2)
print('>')
print(student_1 > student_2)
print('<=')
print(student_1 <= student_2)
print('>=')
print(student_1 >= student_2)

print('\nСравнение lecturer_1 и lecturer_2 по средней оценке:')
print('==')
print(lecturer_1 == lecturer_2)
print('!=')
print(lecturer_1 != lecturer_2)
print('<')
print(lecturer_1 < lecturer_2)
print('>')
print(lecturer_1 > lecturer_2)
print('<=')
print(lecturer_1 <= lecturer_2)
print('>=')
print(lecturer_1 >= lecturer_2)

print('\nСредняя оценка всех студентов на курсе')
print('Java:')
students_avr_grade(all_students, 'Java')
print('Python:')
students_avr_grade(all_students, 'Python')
print('\nСредняя оценка всех лекторов на курсе')
print('Java:')
lecturers_avr_grade(all_lecturers, 'Java')
print('Python:')
lecturers_avr_grade(all_lecturers, 'Python')
