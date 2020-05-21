# Реализуйте структуру данных, представляющую собой расширенную структуру стек.
# Необходимо поддерживать добавление элемента на вершину стека, удаление с вершины стека, и необходимо поддерживать
# операции сложения, вычитания, умножения и целочисленного деления.


class ExtendedStack(list):
    def sum(self):
        return self.append(self.pop() + self.pop())

    def sub(self):
        return self.append(self.pop() - self.pop())

    def mul(self):
        return self.append(self.pop() * self.pop())

    def div(self):
        return self.append(self.pop() // self.pop())
