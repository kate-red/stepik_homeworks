# Вам дана последовательность строк.
# Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.

import re
import sys

pattern = r"z\w{3}z"
for line in sys.stdin:
    line = line.rstrip()
    z = re.findall(pattern, line)
    if z:
        print(line)
