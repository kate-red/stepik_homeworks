# Вам дано описание наследования классов в следующем формате.
# <имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
# Вам необходимо отвечать на запросы, является ли один класс предком другого класса
#
# Важное примечание:
# Создавать классы не требуется.
# Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.

n = int(input())
family_tree = {}


class Parent:
    def __init__(self, parents_name):
        self.parents = parents_name


for j in range(n):  # Создаем словарь для каждого из детелй и родителей
    line = input().split(' : ')
    if len(line) == 1:
        child = line[0]
        family_tree[child] = Parent(None)
    else:
        child, parent = line[0], line[1]
        parents = parent.split()
        family_tree[child] = Parent(parents)
        for i in parents:
            if i not in family_tree:
                # Если родитель не был явно указан ранее, создаем новый ключь с его именем и добавляем в словарь
                family_tree[i] = Parent(None)


def is_parent(parent_name, child_name):
    if parent_name == child_name:
        return 'Yes'
    if family_tree[child_name].parents is None:
        return 'No'
    if parent_name in family_tree[child_name].parents:  # если ребенок - прямой наследник
        return 'Yes'
    else:
        for child_name in family_tree[child_name].parents:  # если ребенок - непрямой наследник (проверка)
            if is_parent(parent_name, child_name) == "Yes":  # поднимаемся вверх по древу с помощью рекурсивной функции
                return "Yes"
        return "No"


n = int(input())
for j in range(n):
    parent, child = input().split()
    print(is_parent(parent, child))
