# Задача 1:
# Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и
# возвращающую самое маленькое целое число y, такое что:
# - y больше или равно x
# - y делится нацело на 5


def closest_mod_5(x):
    return x + 5 - x % 5


# Задача 2:
# Реализуйте программу, которая для заданных n и k вычисляет C(n, k).
# Вашей программе на вход подается строка, содержащая два целых числа n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).
# Ваша программа должна вывести единственное число: C(n, k).

def c_foo(x, y):
    if y == 0:
        return 1
    elif y > x:
        return 0
    else:
        return c_foo(x - 1, y) + c_foo(x - 1, y - 1)


n, k = map(int, input().split())
c = c_foo(n, k)
print(c)
