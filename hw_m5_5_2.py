import json

# data = {
#     'testl': 'testp'
# }
# with open('data.json', 'w') as f:
#     json.dump(data, f)


class Models:
    with open('data.json', 'r') as f:
        data = json.load(f)
    title = 'Какой-то заголовок'
    text = 'Какой-то текст'
    author = 'Какой-то автор'

    def save(self):
        self.data['title'] = self.title
        self.data['text'] = self.text
        self.data['author'] = self.author
        with open('data.json', 'w') as f:
            json.dump(self.data, f)


d = Models()
print(d.save())
print(list(filter(lambda x: not x.startswith('_'), dir(d))))
