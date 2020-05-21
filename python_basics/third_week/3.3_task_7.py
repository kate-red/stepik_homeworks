# Вам дана последовательность строк.
# В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a"
# (регистр не важен), на слово "argh".

import re
import sys

pattern = r"\b[a|A]+\b"  # Шаблон ищет любое слово, состоящее из букв А|a
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        # если в строке есть хоть одно нужное нам слово, заменяем его первое вхождение на "argh"
        print(re.sub(pattern, "argh", line, count=1))
