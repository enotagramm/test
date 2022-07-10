from random import randint as rnd, choice as ch


class Warrior:
    attacks = rnd(10, 30)  # урон если броня разрушена
    attacks_end = rnd(0, 10)  # урон, если боец устал
    defender_arm = rnd(0, 10)  # урон по броне
    defender_arm1 = rnd(0, 20)  # урон после пробития брони
    strings = ch(['отрезал палец', 'засадил нож в печень',
                  'использовал запрещенный приём', 'попал по зубам',
                  'ударил в глаз', 'отрезал ухо', 'сломал нос'])
    strings_arm = ch(['расколол шлем', 'разбил грудак', 'порвал кольчугу'])

    def __init__(self, name, health=100, armor=100, end=100):
        self.name = name
        self.health = health
        self.armor = armor
        self.end = end

    def hit(self, other):
        if self.end >= 10:
            self.end -= 10
            print(f'{self.name} размахивается и теряет очки выносливости')
        else:
            print(f'{self.name} устал')
        other.health -= self.attacks
        print(f'{self.name} {self.strings} на {self.attacks} очков')
        if self.armor <= 0 and self.end <= 0:
            other.health -= self.attacks_end
            print(f'{self.name} {self.strings} на {self.attacks_end} очков')

    def defender(self, other):
        print(f'{other.name}, защищается')
        if self.end >= 10:
            self.end -= 10
            print(f'{self.name} размахивается и теряет очки выносливости')
        else:
            print(f'{self.name} устал')
        if self.armor >= 1 and self.end <= 0:
            other.health -= self.attacks_end
            other.armor -= self.attacks_end
            print(f'{self.name} {self.strings_arm} на {self.attacks_end} очков')
            print(f'{self.name} {self.strings} на {self.attacks_end} очков')
        else:
            other.health -= self.defender_arm1
            other.armor -= self.defender_arm
            print(f'{self.name} {self.strings_arm} на {self.defender_arm} очков')
            print(f'{self.name} {self.strings} {self.defender_arm1} очков')

    def __str__(self):
        return f'{self.name} у него осталось {self.health} здоровья, {self.end} выносливости, {self.armor} брони'


warriors = [Warrior('Викинг'), Warrior('Самурай')]
move = rnd(0, 1)
while True:
    move = not move
    target = rnd(0, 1)
    if target == 0:
        warriors[move].defender(warriors[move - 1])
    else:
        warriors[move].hit(warriors[move - 1])
    if warriors[move - 1].health <= 10:
        winner = warriors[move]
        loser = warriors[move - 1]
        ad = input(f'\nПроиграл {loser}, лежит на песке задыхаясь от полученных травм. Добить его?')
        if ad == 'yes':
            print(f'\n{winner}, добивает его!')
        else:
            print(f'\n{loser} захлебнулся кровью от полученных ран...')
        break
