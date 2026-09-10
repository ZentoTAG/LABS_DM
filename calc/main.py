# Lab_1 Тагиров Вадим ИВТ-25-1б


def print_info():
    print(f"""Калькулятор множеств
          + объединение
          n пересечение
          '\' разность
          / симметрическая разность
          [ дополнение
          """)


def print_set(my_set):
    print("<", *my_set, ">")


sets = {}

U = [x for x in range(-30, 31)]


def calc_answer(formula):
    formula_pies = [i for i in formula]

    choice = int(input("сколько множеств создать: "))
    for i in range(choice):
        name_of_set = input("имя множества: ")
        print('чтобы закончить ввод напишите "stop"')
        el = ""
        temp_list = list()
        while True:
            el = int(input("элемент"))
            if el == 67:
                break
            temp_list.append(el)
            sets[name_of_set] = temp_list

    print(sets)


print(calc_answer("A+B"))
