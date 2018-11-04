"""Project4 Отгадай слово!"""

import random

print("Загадано четырехбуквенное слово из букв А, E, Н, О, С, Т.")
print("Отгадай!")

letters = ['А', 'Е', 'Н', 'О', 'С', 'Т']

word = None
wrong_place = None
x = []

for i in range(4):
    x.extend(random.choice(letters))
attempt = 1
while wrong_place != 0:
    print('Попытка № {}: '.format(attempt), end='')
    word = input()
    true_place = 0
    wrong_place = 0
    for i in range(4):
        if x[i] == word[i]:
            true_place += 1
        else:
            wrong_place += 1
    print('На "своем месте":', true_place)
    print('На "чужом месте":', wrong_place)
    attempt += 1
    if attempt == 11:
        print("Вы проиграли. Если хотите продолжить - напишите: 'ДА' в другом случае - 'НЕТ'")
        answer = input("Ваш ответ: ")
        if answer.upper() == "ДА":
            wrong_place = None
            print('Загадано четырехбуквенное слово из букв А, E, Н, О, С, Т.')
            print('Отгадай!')
            x = []
            for i in range(4):
                x.extend(random.choice(letters))
            attempt = 1

        else:
            print('Удачи, приходите в следующий раз!')
            break

    if wrong_place == 0:
        print("Вы выиграли! Поздравляем!!! Хотите сыграть еще раз? Напишите 'ДА' или 'НЕТ'")
        answer = input("Ваш ответ: ")
        if answer.upper() == "ДА":
            wrong_place = None
            print('Загадано четырехбуквенное слово из букв А, E, Н, О, С, Т.')
            print('Отгадай!')
            x = []
            for i in range(4):
                x.extend(random.choice(letters))
            attempt = 1
        else:
            print("Удачи, приходите в следующий раз!")
            break
