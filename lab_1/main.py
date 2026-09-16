# Lab_1 Тагиров Вадим ИВТ-25-1б
import random
import os

class Set:
    def __init__(self, name, elements):
        self.name = name
        self.elements = elements

    def union(self, other):
        result = self.elements
        for el in other.elements:
            if el not in result:
                result.append(el)
        return result

    def intersect(self, other):
        result = list()
        temp = self.elements + other.elements
        for el in temp:
            if el not in result:
                result.append(el)
        return result

    def diff(self, other):
        pass

    def sym_diff(self, other):
        pass

    def complement(self, universum):
        pass

    def __str__(self):
        if len(self.elements) != 0:
            return f"{self.name} = {{{', '.join(map(str, self.elements))}}}"
        else:
            return f"{self.name} = {{∅}}"


class SetCollection:
    def __init__(self, universum):
        self.U = universum
        self.sets = [Set("A", [1, 2, 3])]

    def add(self, myset):
        if self.find(myset.name) is not None:
            return False
        self.sets.append(myset)
        return True

    def find(self, name):
        for s in self.sets:
            if s.name == name:
                return s
        return None
    
    def in_universum(self, el):
        return el in self.U

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
            print(self.sets.get_set(set_name))
        else: 
            print("такого множества нет")
             
    def input_manual(self, name, count):
        temp = list()
        try:
            while count != 0:
                el = int(input("элемент: "))
                if self.sets.in_universum(el):
                    temp.append(el)
                    count -= 1
                else:
                    print("число не входит в универсум")
            self.sets.add(Set(name, temp))
            print(f"Множество {name} создано")
        except:
            raise ValueError

    def input_random(self):
        pass

    def input_conditions(self):
        pass
    
    def input_set(self, choice):
        pass

    def in_universum(self, el):
        return el in self.sets.U

    def manager(self):
        self.print_info()
        try:
            while True:
                choice = input("действие: ")
                self.clear()
                self.print_info()
                match choice:
                    case "0":
                        break
                    case "1":
                        choice2 = input("1, 2, 3; вручную, случайно, с условиями: ")
                        match choice2:
                            case "1":
                                name = input("имя множества: ")
                                count = int(input("Кол-во элементов: "))
                                self.input_manual(name, count)
                            case "2":
                                name = input("имя множества: ")
                                self.input_random()
                            case "3":
                                print("пока не добавил")
                    case "2":
                        name = input("имя множества: ")
                        self.sets.del_set(name)
                    case "3":
                        name = input("имя множества: ")
                        if self.sets.find(name) is not None:
                            print(self.sets.get_set(name))
                        else:
                            print("Такого множества нет")
                    case "4":
                        pass
                    case _:
                        print("неверный ввод")
                # input("нажмите энтер для продолжения")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")
                        
calc = Calculator()
calc.manager()

    

# manager()
# print(calc_answer("A+B")
