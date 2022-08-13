class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        actual_courses = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        avg_grade = self.get_average_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade}\nКурсы в процессе изучения: {actual_courses}\nЗавершенные курсы: {finished_courses}'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() < other.get_average_grade()
        else:
            return "Ошибка"

    def __le__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() <= other.get_average_grade()
        else:
            return "Ошибка"

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() > other.get_average_grade()
        else:
            return "Ошибка"

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() >= other.get_average_grade()
        else:
            return "Ошибка"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() == other.get_average_grade()
        else:
            return "Ошибка"

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() != other.get_average_grade()
        else:
            return "Ошибка"

    def get_average_grade(self):
        result_avg_grade = 0
        counter = 0

        for courseName in self.courses_in_progress:
            course_grades = self.grades[courseName]
            avg_grade = sum(course_grades) / len(course_grades)

            result_avg_grade += avg_grade
            counter += 1

        return result_avg_grade / counter


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self.get_average_grade
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade}'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() < other.get_average_grade()
        else:
            return "Ошибка"

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() <= other.get_average_grade()
        else:
            return "Ошибка"

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() > other.get_average_grade()
        else:
            return "Ошибка"

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() >= other.get_average_grade()
        else:
            return "Ошибка"

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() == other.get_average_grade()
        else:
            return "Ошибка"

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() != other.get_average_grade()
        else:
            return "Ошибка"

    def get_average_grade(self):
        result_avg_grade = 0
        counter = 0

        for courseName in self.courses_attached:
            course_grades = self.grades[courseName]
            avg_grade = sum(course_grades) / len(course_grades)

            result_avg_grade += avg_grade
            counter += 1

        return result_avg_grade / counter

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress and course in self.courses_attached:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# john_snow = Student('John', 'Snow', 'male')
# princess_lea = Student('Princess', 'Lea', 'female')
# howard_wolowitz = Mentor('Howard', 'Wolowitz')
# isak_newton = Mentor('Isak', 'Newton')
# luke_skywalker = Lecturer('Luke', 'Skywalker')
# sheldon_cooper = Lecturer('Sheldon', 'Cooper')
# peter_pen = Reviewer('Peter', 'Pen')
# anton_chekhov = Reviewer('Anton', 'Chekhov')

if __name__ == '__main__':
    peter_pen = Reviewer('Peter', 'Pen')
    peter_pen.courses_attached = ['Python', 'Git']

    john_snow = Student('John', 'Snow', 'male')
    john_snow.courses_in_progress = ['Python', 'JS']
    john_snow.grades['Python'] = [10, 10]
    john_snow.grades['JS'] = [1, 1]

    peter_pen.rate_hw(john_snow, 'Git', 8)
    print(john_snow.grades)
    