# Создайте класс точка Point, позволяющий работать с координатами (x, y).
# Добавьте необходимые методы класса.

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt = Point(1, 2)
print(pt.get_coords())

print(pt.__dict__) # либо так, не совсем понял, что от меня требуется


