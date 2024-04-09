import unittest

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]
mentors = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

courses_list = []
for course, mentor, duration in zip(courses, mentors, durations):
    course_dict = {"title": course, "mentors": mentor, "duration": duration}
    courses_list.append(course_dict)

durations_dict = {}

for id, course in enumerate(courses_list):
    key = course['duration']
    durations_dict.setdefault(key, [])
    durations_dict[key].append(id)

durations_dict = dict(sorted(durations_dict.items()))

for duration, ids in list(durations_dict.items()):
    for id in ids:
        a = courses_list[id]['title']
        print(f"{a} - {duration} месяцев")


class TestCourseDuration(unittest.TestCase):

    def test_course_duration_order(self):
        expected_output = [
            "Python-разработчик с нуля - 12 месяцев",
            "Java-разработчик с нуля - 14 месяцев",
            "Fullstack-разработчик на Python - 20 месяцев",
            "Frontend-разработчик с нуля - 20 месяцев"
        ]
        actual_output = []
        for duration, ids in durations_dict.items():
            for id in ids:
                course_title = courses_list[id]['title']
                actual_output.append(f"{course_title} - {duration} месяцев")

        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
