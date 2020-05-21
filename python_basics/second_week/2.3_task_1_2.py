# 1
# Одним из самых часто используемых классов в Python является класс filter. Он принимает в конструкторе два аргумента a
# и f – последовательность и функцию, и позволяет проитерироваться только по таким элементам x из последовательности a,
# что f(x) равно True. Будем говорить, что в этом случае функция f допускает элемент x, а элемент x является допущенным.
#
# В данной задаче мы просим вас реализовать класс multifilter, который будет выполнять ту же функцию, что и стандартный
# класс filter, но будет использовать не одну функцию, а несколько.

# -*- coding: utf-8 -*-


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


class multifilter:

    def judge_half(self, pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg


    def judge_any(self, pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos >= 1


    def judge_all(self, pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable  # iterable - исходная последовательность
        self.funcs = funcs  # funcs - допускающие функции
        self.judge = judge  # judge - решающая функция
        self.current_i = 0

    def __iter__(self):
        return self
        # возвращает итератор по результирующей последовательности

    def __next__(self):
        if self.current_i < len(self.iterable):
            pos = 0
            neg = 0
            current_element = self.iterable[self.current_i]
            for func in self.funcs:
                if func(current_element):
                    pos += 1
                else:
                    neg += 1
            self.current_i += 1
            if self.judge(self, pos, neg):
                return current_element
            else:
                return next(self)
        else:
            raise StopIteration


# 2
# Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания,
# начиная с числа 2.

import itertools


def factorial(n):
    out = 1
    for i in range(2, n+1):
        out *= i
    return out


def primes():
    start = 2

    while True:
        if (factorial(start - 1) + 1) % start == 0:
            start += 1
            yield start - 1
        else:
            start += 1
