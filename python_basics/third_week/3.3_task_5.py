# Вам дана последовательность строк.
# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

import re
import sys

pattern = r"((\b\w+)\2)\b"
for line in sys.stdin:
    line = line.rstrip()
    if re.findall(pattern, line):
        print(line)
