import random


# 1: Создайте функцию, принимающую на вход имя, возраст
# и город проживания человека. Функция должна возвращать строку вида
# «Василий, 21 год(а), проживает в городе Москва»

def info(name, age, home_city):
    return str(f'{name}, {age} год(а), проживает в городе {home_city}')


print(info('vlad', 26, 'Moscou'))


# 2: Создайте функцию, принимающую на вход 3 числа
# и возвращающую наибольшее из них.

def max_number(*args):
    return max(args)


print(max_number(1, 2, 5))


# 3: Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50.
# ### Поэкспериментируйте с значениями урона и жизней по желанию.
# ### Теперь надо создать функцию attack(person1, person2).
# Примечание: имена аргументов можете указать свои. ###
# Функция в качестве аргумента будет принимать атакующего и атакуемого.
# ### В теле функция должна получить параметр damage атакующего и
# отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.
# 4: Давайте усложним предыдущее задание.
# Измените сущности, добавив новый параметр - armor = 1.2
# (величина брони персонажа)


def attack_players(gamer_1, gamer_2):
    attack_lvl = random.randint(1, gamer_1['damage'])

    print(f'{gamer_1["name"]} наносит удар по {gamer_2["name"]}')
    attack_power = armor_players(attack_lvl, gamer_2['armor'])
    damage = gamer_2['health'] - attack_power
    gamer_2['health'] = round(damage, 2)
    print(f'{gamer_1["name"]} нанес {attack_lvl} урона по {gamer_2["name"]} \n'
          f'У {gamer_2["name"]} осталось {gamer_2["health"]} очков здоровья')


def armor_players(attack, armor):
    return attack / armor


user_1 = input('Введите имя игрока 1: ')
user_2 = input('Введите имя игрока 2: ')
winner = None
rounds = 1

player_1 = {'name': user_1,
            'health': 100,
            'damage': 50,
            'armor': 2.2}

player_2 = {'name': user_2,
            'health': 100,
            'damage': 50,
            'armor': 2.2}

print(f'В бою учавствуют {user_1} и {user_2}')

while player_1['health'] > 0 and player_2['health'] > 0:
    start_fight = input('В бой? (да, нет): ')
    if start_fight.lower() == 'да':
        print('Бой начинается!')
    else:
        print('Бой отменен по инициативе игроков')
        break
    print(f'Раунд {rounds}')
    rounds += 1
    attack_players(player_1, player_2)
    if player_2['health'] > 0:
        print(f'ход игрока {player_2["name"]}?')
    elif player_2['health'] <= 0:
        winner = player_1['name']
        continue
    attack_players(player_2, player_1)
    if player_1['health'] > 0:
        print(f'ход игрока {player_1["name"]}')
    elif player_1['health'] <= 0:
        winner = player_2['name']
        continue
else:
    print(f'Победил игрок {winner}')
