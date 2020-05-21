# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле
# name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

import json


class Children:
    """
    Класс для удобного хранения имен наследников
    """

    def __init__(self, children_names: list):
        self.children_names = children_names

    def __repr__(self):
        """
        Функция для отображения имен в виде списка
        """
        if self.children_names is None or len(self.children_names) == 0:
            return "No children"
        return ", ".join(self.children_names)

    def append_child(self, child_name: str):
        """
        Функция для добавляения имени нового наследника
        """
        self.children_names.append(child_name)


def children_number(family_name: str, all_children_set: set):
    """
    Функция записывает всех прямых и непрямых наследников в all_children_set
    """
    if len(family_tree[family_name].children_names) > 0:  # Если лист с наследниками не пустой
        for name in family_tree[family_name].children_names:  # Циклом прохожимся по всем наследникам
            all_children_set.add(name)  # добавляем имя в set
            # Вызываем рекурсивную функцию для нахождения наследников наследника
            children_number(name, all_children_set)


json_tree_str = input()
json_tree_from_str = json.loads(json_tree_str)  # Переводим считанную строку в читаемый питоном формат
family_tree = {}  # Создаем пустой словарь для хранения пары родитель: дети

for family in json_tree_from_str:
    child = family['name']
    parents = family['parents']
    if child not in family_tree:  # Если ключа еще нет в списке, создаем новую пару
        family_tree[child] = Children([])
    for parent in parents:
        if parent not in family_tree:
            family_tree[parent] = Children([])
        family_tree[parent].append_child(child)  # Добавляем имя наследника родителя (нам нужен обратный порядок)

keys_family_tree = list(family_tree.keys())  # Список с ключами словаря
keys_family_tree.sort()  # Сортируем ключи в лекикографическом порядке

for family_name in keys_family_tree:
    all_children = set()
    children_number(family_name, all_children)
    print("{0} : {1}".format(family_name, len(all_children) + 1))  # Добавляем к числу наследников 1 (сам родитель)
