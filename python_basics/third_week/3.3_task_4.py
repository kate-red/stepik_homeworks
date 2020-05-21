# Вам дана последовательность строк.
# Выведите строки, содержащие обратный слеш "\﻿".

import re
import sys

pattern = r"\\"
for line in sys.stdin:
    line = line.rstrip()
    slash = re.findall(pattern, line)
    if slash:
        print(line)
