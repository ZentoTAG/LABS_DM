# Lab_1 Тагиров Вадим ИВТ-25-1б
import random

# константы, глобальные переменные
sets = {"A": [1, 2, 3]}
U = [x for x in range(-30, 31)]

def print_info():
    print("Это мой калькулятор производных, введите цифру для выбора действия")
    print(
"""
0 - завершить пограмму
1 - создать и ввести множество
2 - удалить множество
3 - вывести множество
4 - ввод математической формулы
""")

def in_universum(el):
    return el in U

def get_set(name):
    return sets[name]

def is_unique(el, myset):
    if el not in myset:
        return True
    return False

def print_set():
    set_name = input("Имя множества: ")
    if set_name in sets:
        print(f"{set_name} = {{{', '.join(map(str, sets[set_name]))}}}")
    else: 
        print("такого множества нет")

def input_manual():
    name = input("Имя множества: ")
    count = int(input("Кол-во элементов множества: "))
    temp = list()
    try:
        while count != 0:
            el = int(input("элемент: "))
            if all([in_universum(el), is_unique(el, temp)]):
                temp.append(el)
                count -= 1
        sets[name] = temp
    except:
        raise ValueError
def input_random():
    pass

def input_conditions():
    pass

def input_set():
    print("""выберите способ ввода множества,
    1 - ввод вручную,
    2 - случайное множество,
    3 - задание условий
          """)
    choice = int(input("Действие: "))
    match choice:
        case 1:
            input_manual()
        case 2:
            input_random()
        case 3:
            input_conditions()


def del_set():
    current_set_name = input("Введите имя множества: ")
    if current_set_name in sets:
        print("Множество ", current_set_name, " удалено")
        del sets[current_set_name]

def formula_parser():
    formula = input("")
    formula_elements = list(map(int, formula.split()))
    print(formula_elements)
   
def manager():
    print_info()
    while True:
        try:
            choice = int(input("выбор: "))
            match choice:
                case 0:
                    break
                case 1:
                    input_set()
                case 2:
                    del_set()
                case 3:
                    print_set()
                case 4:
                    formula_parser()
                 
        except:
             print("где то ошибка")
             

manager()
# print(calc_answer("A+B")
