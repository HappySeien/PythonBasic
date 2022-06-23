import os


def mkdir():
    for i in range(1, 10):
        os.mkdir(f'dir_{i}')


def rmdir():
    for i in range(1, 10):
        os.rmdir(f'dir_{i}')
