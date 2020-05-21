# Вам дана последовательность строк.
# В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите
# полученные строки.

import re
import sys

pattern = r"human"
for line in sys.stdin:
    line = line.rstrip()
    if re.findall(pattern, line):
        print(re.sub(pattern, "computer", line))
    else:
        print(line)
