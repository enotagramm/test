# Создайте класс StringVar для работы со строковым типом данных, содержащий методы set() и get().
# Метод set() служит для изменения содержимого строки,
# get() – для получения содержимого строки. Создайте объект типа StringVar и протестируйте его методы.

class StringVar:

    def __init__(self):
        self.s = ''

    def set(self, line):
        self.s = line

    def get(self):
        return self.s


s = StringVar()
s.set('chiken fly')

print(s.get())
