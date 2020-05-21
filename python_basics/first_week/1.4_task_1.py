# Задача
# Реализуйте программу, которая будет эмулировать работу с пространствами имен.
# Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.
#
# В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.
#
# Вашей программе на вход подаются следующие запросы:
#
# create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
# add <namespace> <var> – добавить в пространство <namespace> переменную <var>
# get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из
# пространства <namespace>, или None, если такого пространства не существует

rep = int(input())
scopes = {'global': {'parent': None, 'variables': []}}


def get(namespace, argument):
    if argument in scopes[namespace]['variables']:
        return namespace
    elif scopes[namespace]['parent'] is None:
        return None
    else:
        return get(scopes[namespace]['parent'], argument)


for _ in range(rep):
    cmd, namesp, arg = (str(i) for i in input().split())
    if cmd == 'create':
        if namesp not in scopes:
            scopes[namesp] = {}
            scopes[namesp]['parent'] = arg
            scopes[namesp]['variables'] = []
    elif cmd == 'add':
        variables = scopes[namesp]['variables']
        variables.append(arg)
    elif cmd == 'get':
        print(get(namesp, arg))
