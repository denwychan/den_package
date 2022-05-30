# Code for love score

from random import randint

def love_score(name1, name2):
    rand_number = randint(0, 100)
    score = ((len(name1) * len(name2) * rand_number) / (len(name1) * len(name2) * 100)) * 100
    return f'{name1} and {name2} your love score is {score} xxx'
