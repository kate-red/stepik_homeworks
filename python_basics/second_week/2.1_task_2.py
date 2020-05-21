# Вам дано описание наследования классов исключений в следующем формате.
# <имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
# Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.
#
# Антон написал код, который выглядит следующим образом:

# try:
#    foo()
# except <имя 1>:
#    print("<имя 1>")
# except <имя 2>:
#    print("<имя 2>")
# ...

# Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить, так как ранее в коде
# будет пойман их предок. Но Антон не помнит какие исключения наследуются от каких. Помогите ему выйти из неловкого
# положения и напишите программу, которая будет определять обработку каких исключений можно удалить из кода.
#
# Важное примечание:
# В отличие от предыдущей задачи, типы исключений не созданы.
# Создавать классы исключений также не требуется
# Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить, потому что мы уже ранее
# где-то поймали их предка.
#
# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов исключений.
#
# В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й
# класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от
# себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.
#
# В следующей строке содержится число m - количество обрабатываемых исключений.
# Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
# Гарантируется, что никакое исключение не обрабатывается дважды.
#
# Формат выходных данных
# Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, не изменив при этом
# поведение программы. Имена следует выводить в том же порядке, в котором они идут во входных данных.

# put your python code here
n = int(input())
exception_hierarchy = {}


class Child:
    """Создаем класс детей, которые содержат список своих родителей"""

    def __init__(self, child_parents):
        self.parents = child_parents


for _ in range(n):
    line = input().split(' : ')
    if len(line) == 1:
        child = line[0]
        exception_hierarchy[child] = Child(None)
    else:
        child, father = line[0], line[1]
        parents = father.split()
        exception_hierarchy[child] = Child(parents)
        for p in parents:
            if p not in exception_hierarchy:
                exception_hierarchy[p] = Child(None)

exception_list = set()  # Записываем обработанные ошибки, кроме тех, которые были запринтованы


def need_del_exception(exception):
    if check_exception(exception):  # Запускам функцию проверки
        print(exception)  # Функция вернула True - предки exception есть в exception_list - принтуем exception
    else:
        exception_list.add(exception)  # Если родителей exception нет в exception_list - добавляем exception


def check_exception(exce):  # Проверка есть ли предки в exception_list
    if exce in exception_list:
        return True
    if exception_hierarchy[exce].parents is None:
        return False
    # Рекурсивная функция проверки наличия предков предков в exception_list
    for ex in exception_hierarchy[exce].parents:
        if check_exception(ex):
            return True
    return False


n = int(input())
for _ in range(n):
    error = input()
    need_del_exception(error)
