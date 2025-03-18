data = {
    "students" : [
        {
            "name":"John",
            "age":18 ,
            "courses":[
                {
                    "name": "math",
                    "grade": 4
                },
                {
                    "name": "English",
                    "grade": 5

                }
            ]
        },
        {
            "name":"Jane",
            "age":19 ,
            "courses":[
                {
                    "name": "math",
                    "grade": 5
                },
                {
                    "name": "English",
                    "grade": 4

                }
            ]
        }
    ]
}

students = data["students"]
count_students = len(students)

total_age = sum(student["age"] for student in students)
average_age = total_age / count_students

course_grades = {}
for student in students:
    for course in student["courses"]:
        course_name = course["name"]
        grade = course["grade"]
        if course_name not in course_grades:
            course_grades[course_name] = []
        course_grades[course_name].append(grade)

math_avg = sum(course_grades["math"]) / len(course_grades["math"])
english_avg = sum(course_grades["English"]) / len(course_grades["English"])

all_grades = [course["grade"] for student in students for course in student["courses"]]
overall_avg = sum(all_grades) / len(all_grades)

print(f"Количество студентов: {count_students}")
print(f"Средний возраст студентов: {average_age}")
print(f"Средний балл по математике: {math_avg:.1f}")
print(f"Средний балл по английскому: {english_avg:.1f}")
print(f"Общий средний балл по всем курсам: {overall_avg:.1f}")