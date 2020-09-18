from sys import getsizeof
import datetime
import re
import os
os.getcwd()


def get_array():
    words = []
    with open('/home/serg/PycharmProjects/IntroductionToAlgorithms/data/puskin.txt', encoding='utf8') as book:
        for row in book:
            words.extend(
                list(map(
                    lambda x: x.lower(),
                    filter(None, re.findall(r'[a-zA-Z]*', row))
                ))
            )
    print('words count: ', len(words))
    print('size array: ', getsizeof(words))
    print('unique words: ', len(set(words)))
    print('first 50 words: ', words[:50])

    return words


def run(func, array):
    START = datetime.datetime.now()
    print('=' * 20, f' START {func} ', '=' * 20)
    print('START: ', START)
    print('first 50 sorted words:', func(array[:])[:50])
    FINISH = datetime.datetime.now()
    print('FINISH: ', FINISH)
    print('RESULT: ', FINISH - START)

    print('=' * 20, ' START sorted ', '=' * 20)
    START = datetime.datetime.now()
    print('START: ', START)
    print('first 50 sorted words:', sorted(array[:])[:50])
    FINISH = datetime.datetime.now()
    print('FINISH: ', FINISH)
    print('RESULT: ', FINISH - START)
