"""
Напишите программу печатающую бейджики учеников.
Программа запрашивает ввод числа учеников и печатает каждому бейджик. Бейдж содержит название учебного заведения:
«Колледж Сириус», поле для имени:
«Имя: ____» и поле для школы:
«Группа: ____». Напиши программу, печатающую бейджики студентов как на картинке. В завершении программа должна печатать:
«Готово! Заберите бейджики.»
Функция должна принимать имя и группу ученика.
"""

def print_labl():
    print('Колледж Сириус')
    print(input("Имя:"))
    print(input("Группа:"))


print("Автомат для печати бейджика")
amout = int(input("Число учеников:"))
for i in range(amout):
    print_labl()
print("Готово! Заберите бейджики.")