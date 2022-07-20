import json


class Model:
    def __init__(self, title='1', text='2', author='3'):
        self.title = title
        self.text = text
        self.author = author

    def save(self):
        with open('data.json', 'w') as f:
            json.dump(json.dumps(self.__dict__), f)
        with open('data.json') as f:
            print(f.read())


c1 = Model('Hi')
print(c1.save())
print(dir(c1))
