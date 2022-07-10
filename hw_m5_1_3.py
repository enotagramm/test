from random import randint, choice


class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def hit(self, two):
        hit = randint(1, 20)
        if hit < 5:
            strings = choice(['плюнул в лицо', 'швырнул песок в глаза', 'укусил за ухо'])
        elif 5 < hit < 15:
            strings = choice(['попал по зубам', 'ударил в глаз', 'отрезал ухо', 'сломал нос'])
        elif 15 <= hit <= 18:
            strings = choice(['отрезал руку', 'засадил нож в печень', 'использовал запрещенный приём'])
        else:
            strings = 'УДАРИЛ ПО МЕЗИНЦУ!'
        print(f'{self.name} {strings} на {hit} очков')
        two.health -= hit

    def __str__(self):
        return f'{self.name} у него осталось {self.health} здоровья'


warriors = [Warrior('Викинг'), Warrior('Самурай')]
move = randint(0, 1)

while True:
    move = not move
    warriors[move].hit(warriors[move - 1])
    if warriors[move - 1].health <= 0:
        winner = warriors[move]
        break
print(f'\nПобедил {winner}')