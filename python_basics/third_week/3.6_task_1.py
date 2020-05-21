# Вам дано описание пирамиды из кубиков в формате XML.
# Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
# Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.
#
# Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность
# 1. Кубики, расположенные прямо под ним, имеют ценность
# 2. Кубики, расположенные прямо под нижележащими кубиками, имеют ценность
# 3. И т. д.
#
# Ценность цвета равна сумме ценностей всех кубиков этого цвета.
#
# Выведите через пробел три числа: ценности красного, зеленого и синего цветов.

from xml.etree import ElementTree

colors = {"red": 0, "blue": 0, "green": 0}  # dict for color score storage
counter = 1  # counter for counting color's score


def get_color_score(f_root, f_counter):
    """
    :param f_root: current root level
    :param f_counter: root level counter
    """
    f_counter += 1  # going one level deeper
    for f_child in f_root:  # check colors on this level one by one
        color = f_child.get("color")
        colors[color] += f_counter  # change the color's value in dict
        get_color_score(f_child, f_counter)  # call recursive function to check children of f_child

user_input = input()
root = ElementTree.fromstring(user_input)  # reed tree from a string
root_color = root.get("color")  # get first-level cube color
colors[root_color] += counter  # counter = 1
get_color_score(root, counter)  # apply function to get the rest of scores
print("{0} {1} {2}".format(colors["red"], colors["green"], colors["blue"]))
