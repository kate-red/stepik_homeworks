# Вам дана последовательность строк.
# В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
# Буквой считается символ из группы \w.

import re
import sys

pattern = r"\b(\w)(\w)"
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, r"\2\1", line))
