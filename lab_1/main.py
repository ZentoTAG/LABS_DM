# Lab_1 Тагиров Вадим ИВТ-25-1б
import random
import os


def format_set(elements):
    if not elements:
        return "{∅}"
    return "{" + ", ".join(map(str, elements)) + "}"
    
class Set:
    def __init__(self, name, elements):
        self.name = name
        self.elements = elements

    def union(self, other):
        result = self.elements.copy()
        for el in other.elements:
            if el not in result:
                result.append(el)
        return result

    def intersect(self, other):
        result = []
        for el in self.elements:
            if el in other.elements and el not in result:
                result.append(el)
        return result

    def diff(self, other):
        result = []
        for el in self.elements:
            if el not in other.elements and el not in result:
                result.append(el)
        return result

    def sym_diff(self, other):
        result = []
        for el in self.elements:
            if el not in other.elements and el not in result:
                result.append(el)
        for el in other.elements:
            if el not in self.elements and el not in result:
                result.append(el)
        return result

    def __str__(self):
        if len(self.elements) != 0:
            return f"{self.name} = {{{', '.join(map(str, self.elements))}}}"
        else:
            return f"{self.name} = {{∅}}"


class SetCollection:
    def __init__(self, universum):
        self.U = universum
        self.sets = []
        self.operators = (("+"))

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

    def complement(self, name):
        s = self.find(name)
        if s is None:
            return None
        result = [x for x in self.U if x not in s.elements]
        return Set(f"¬{name}", result)

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
                if self.sets.in_universum(el) and el not in temp:
                    temp.append(el)
                    count -= 1
                else:
                    print("Число вне универсума или уже есть")
            self.sets.add(Set(name, sorted(temp)))
            print(f"Множество {name} создано")
        except:
            raise ValueError

    def input_random(self, name, count):
        temp = list()
        U_copy = self.sets.U.copy()
        try:
            while count != 0:
                el = random.choice(self.sets.U)
                if self.sets.in_universum(el):
                    temp.append(el)
                    count -= 1 
            self.sets.add(Set(name, sorted(temp)))
            print(f"Множество {name} создано")
        except:
            print("где-то ошибка")
                
    def input_conditions(self, name, condition):
        temp = list()
        U_copy = self.sets.U.copy()
        try:
            if "нечёт" in condition:
                temp = [x for x in U_copy if x % 2 != 0]
            elif "чёт" in condition: 
                temp = [x for x in U_copy if x % 2 == 0]
            if "неотриц" in condition:
                temp = [x for x in U_copy if x >= 0]
            elif "отриц" in condition:
                temp = [x for x in U_copy if x < 0]
            if "кратн" in condition:
                choice = input("кратно: ")
                temp = [x for x in U_copy if x % int(choice) == 0]
            if "диап" in condition:
                x, y = list(map(int, input("диап в виде x y: ").split()))
                temp = [el for el in range(x, y+1) if self.sets.in_universum(el)]
            self.sets.add(name, sorted(temp))
            print(f"Множество {name} создано")
        except:
            raise ValueError("ошибка ввода значения")
    
    def input_set(self, choice):
        pass

    def in_universum(self, el):
        return el in self.sets.U

    def formula_parser(self, formula):
        formula = formula.replace(" ", "")

        save = False
        if "=" in formula:
            parts = formula.split("=", 1)
            left = parts[0]
            formula = parts[1]
            save = True

        result = self.evaluate(formula)
        if result is None:
            print("Ошибка в формуле")
            return

        for s in self.sets.sets[:]:
            if s.name.startswith("_temp_"):
                self.sets.sets.remove(s)

        if save:
            self.sets.del_set(left)
            self.sets.add(Set(left, result.elements))
            print(f"{left} = {format_set(result.elements)}")
        else:
            print(f"{format_set(result.elements)}")

    def evaluate(self, formula):
        formula = formula.replace(" ", "")

        while "(" in formula:
            start = formula.rfind("(")
            end = formula.find(")", start)
            if end == -1:
                print("Незакрытая скобка")
                return None

            inner = formula[start + 1:end]
            inner_result = self.evaluate(inner)
            if inner_result is None:
                return None

            temp_name = f"_temp_{start}"
            self.sets.add(Set(temp_name, inner_result.elements))
            formula = formula[:start] + temp_name + formula[end + 1:]

        tokens = []
        i = 0
        while i < len(formula):
            if formula[i] in "+-*^!":
                tokens.append(formula[i])
                i += 1
            else:
                j = i
                while j < len(formula) and formula[j] not in "+-*^!":
                    j += 1
                tokens.append(formula[i:j])
                i = j

        if not tokens:
            print("Пустая формула")
            return None

        if tokens[0] == "!":
            name = tokens[1]
            result = self.sets.complement(name)
            if result is None:
                print(f"Множество {name} не найдено")
                return None
            print(f"!{name} = {result.elements}")
            i = 2
        else:
            result = self.sets.get_set(tokens[0])
            if result is None:
                print(f"Множество {tokens[0]} не найдено")
                return None
            i = 1

        while i < len(tokens):
            op = tokens[i]
            name = tokens[i + 1]
            other = self.sets.get_set(name)
            if other is None:
                print(f"Множество {name} не найдено")
                return None

            old = result.elements.copy()

            if op == "+":
                result = Set("temp", result.union(other))
            elif op == "*":
                result = Set("temp", result.intersect(other))
            elif op == "-":
                result = Set("temp", result.diff(other))
            elif op == "^":
                result = Set("temp", result.sym_diff(other))

            print(f"{old} {op} {other.elements} = {result.elements}")

            i += 2

        return result
        
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
                                count = int(input("кол-во элементов: "))
                                self.input_random(name, count)
                            case "3":
                                name = input("имя множества: ")
                                condition = input("условие: ")
                                self.input_conditions(name, condition)
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
                        name = input("формула: ")
                        self.formula_parser(name)
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
