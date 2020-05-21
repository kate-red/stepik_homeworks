# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
#
# Выведите одно число – количество вхождений строки t в строку s.

s = input()
t = input()
counter = 0
for i in range(len(s)):
    if t == s[i:i + (len(t))]:
        counter += 1
print(counter)
