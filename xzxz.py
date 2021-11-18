from prettytable import PrettyTable

table = PrettyTable()
students_grades = []


def get_grade(elements):
    students_grades.append([elements[0], elements[3]])
    return elements


def good_students(students):
    best_students = []
    all_grades = [grade[1] for grade in students_grades]
    avg_grade = round(sum(all_grades) / len(all_grades))
    print('средняя оценка', avg_grade)
    for grade in students:
        if grade[1] >= avg_grade:
            best_students.append(grade[0])
    print('Лучшие ученики:',', '.join(best_students))


table.field_names = ["Name", "City name", 'Age', "Grade"]
table.add_rows(
    [
        get_grade(["Лёха", 'Балашиха', 18, 5]),
        get_grade(["Киря", 'Электрогорск', 17, 4]),
        get_grade(["Артем", 'Электросталь', 17, 5]),
        get_grade(["Даня", 'Электросталь', 17, 4]),
        get_grade(["Максим", 'Электрогорск', 15, 3]),
        get_grade(["Валодя", 'Дуброво', 16, 2]),
        get_grade(["Topson", 'na dne', 31, 1]),
    ]
)

print(table)
good_students(students_grades)
