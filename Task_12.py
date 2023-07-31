# Создайте класс студента.
# * Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# * Названия предметов должны загружаться из файла CSV при создании экземпляра. 
# Другие предметы в экземпляре недопустимы.
# * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# * Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по 
# оценкам всех предметов вместе взятых.

import csv


class Check:
    def check(self, value):
        if value != value.capitalize() or not value.isalpha():
            raise 'Строка должна начинаться с заглавной буквы и содержать только буквы'

    def __set_name__(self, _, name):
        self.name = name

    def __get__(self, instance, _):
        print(self.name)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.check(value)
        instance.__dict__[self.name] = value


class Student:
    firstname = Check()
    lastname = Check()
    patronymic = Check()

    def __init__(self, firstname, lastname, patronymic):
        self.firstname = firstname
        self.lastname = lastname
        self.patronymic = patronymic

    def cal_average(self):
        dict_average = {}
        with open('lessons.csv', 'r', encoding='utf-8', newline='') as file:
            filereader = csv.DictReader(file, delimiter='/')
            for line in filereader:
                grades = list(map(int, line['Оценки'].split()))
                tests = list(map(int, line['Тесты'].split()))
                av_grades = sum(grades) / len(grades)
                av_tests = sum(tests) / len(tests)
                dict_average[line['Предметы']] = (
                    '%.2f' % av_grades, '%.2f' % av_tests)

        for k, v in dict_average.items():
            print(
                f'Предмет: {k}, средняя оценка: {v[0]}, средний балл теста: {v[1]}')

        sum_grades = sum([float(k[0]) for _, k in dict_average.items()])
        sum_test = sum([float(k[1]) for _, k in dict_average.items()])

        print("Средняя оценка по всем предметам:", '%.2f' % (sum_grades / len(dict_average)),
              "Средний балл по всем тестам:", '%.2f' % (sum_test / len(dict_average)))


student = Student('Константин', 'Лазарев', 'Евгеньевич')
print(student.__dict__)
student.cal_average()
