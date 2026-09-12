# Lab_1 Тагиров Вадим ИВТ-25-1б
import random

# константы, глобальные переменные
sets = {"A": [1, 2, 3]}
U = [x for x in range(-30, 31)]

def in_universum(el):
    return el in U

def get_set(name):
    return sets[name]

def is_unique(el, myset):
    if el not in myset:
        return True
    return False


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

def union(name1, name2):
    result = list()
    for el in [sets[name1] + sets[name2]]:
        if el not in result:
            result.append(el)


# def manager():
#     print_info()
#     while True:
#         try:
#             choice = int(input("выбор: "))
#             match choice:
#                 case 0:
#                     break
#                 case 1:
#                     input_set()
#                 case 2:
#                     del_set()
#                 case 3:
#                     print_set()
#                 case 4:
#                     formula_parser()
#                  
#         except:
#              print("где то ошибка")
#

class Set:
    def __init__(self, name, elements):
        self.name = name
        self.elements = elements

    def union(self, other):
        pass

    def intersect(self, other):
        pass

    def diff(self, other):
        pass

    def sym_diff(self, other):
        pass

    def complement(self, other):
        pass

    def __str__(self):
        return f"{self.name} = {{{', '.join(map(str, self.elements))}}}"

class SetCollection:
    def __init__(self, universum):
        self.U = universum
        self.sets = []

    def add(self, myset):
        self.sets.append(myset)
    
    def find(self, name):
        for s in self.sets:
            if s.name == name:
                return s
        return None

    def get_set(self, name):
        return self.find(name)

    def del_set(self, name):
        s = self.find(name)
        if s is not None:
            self.sets.remove(s)
            return True
        return False

    def in_SetCollection(self, name):
        return self.find(name) is not None
 
class Calculator:
    def __init__(self):
        self.sets = SetCollection(list(range(-30, 31)))

    def print_info(self):
        print(
"""Это мой калькулятор производных, введите цифру для выбора действия
0 - завершить пограмму
1 - создать и ввести множество
2 - удалить множество
3 - вывести множество
4 - ввод математической формулы
    """)

    def print_set(self, set_name):
        if self.sets.in_SetCollection(set_name):

        else: 
            print("такого множества нет")
             
    def input_manual(self, name, count):
        temp = list()
        try:
            while count != 0:
                el = int(input("элемент: "))
                if all([in_universum(el), is_unique(el, temp)]):
                    temp.append(el)
                    count -= 1
            self.sets[name] = temp
        except:
            raise ValueError

    def input_random(self):
        pass

    def input_conditions(self):
        pass
    
    def input_set(self, choice):
        pass

    def in_universum(self, el):
        return el in self.U


    

# manager()
# print(calc_answer("A+B")
