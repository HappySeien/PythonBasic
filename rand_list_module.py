from random import choice


def rand_el(lst):
    if len(lst) == 0:
        print('None')
    else:
        print(choice(lst))


if __name__ == '__main__':
    rand_lst = [1, 2, 3, 4, 5]
    rand_el(rand_lst)
