import random

print('Загадайте число от 1 до 100')
user_answer = None
min_number = 1
max_number = 100

while user_answer != '=':
    ai_answer = random.randint(min_number, max_number)
    user_answer = input(f'Если да, введите "=",'
                        f'если ваше число больше, введите ">",'
                        f'если ваше меньше, введите "<" \n'
                        f'Это ваше число {ai_answer}?: ')

    if user_answer == '<':
        max_number = ai_answer - 1
    elif user_answer == '>':
        min_number = ai_answer + 1
else:
    print('Ура я угадал!')
