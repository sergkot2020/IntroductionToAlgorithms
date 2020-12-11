"""
Task from Amazon

Given a 2D board that represents a word search puzzle and a string word,
return whether or the given word can be formed in the puzzle by only connecting cells horizontally and vertically.

board =
[
  ['C','A','T','F'],
  ['B','G','E','S'],
  ['I','T','A','E']
]
word = "CAT", return true
word = "TEA", return true
word = "SEAT", return true
word = "BAT", return false
"""
from collections import defaultdict

board_ = [
    ['C', 'A', 'T', 'F'],
    ['B', 'G', 'E', 'S'],
    ['I', 'T', 'A', 'E']
]

cache_ = defaultdict(list)

for y, row in enumerate(board_):
    for x, symbol in enumerate(row):
        cache_[symbol].append((x, y))


def function(cache, coordinates=None, word=None):
    is_correct = False

    if not coordinates:
        is_correct = True

    s = word[0]

    for x_, y_ in cache[s]:

        if coordinates:
            x, y = coordinates
            is_correct = (abs(x - x_) == 1 and y == y_) or (abs(y - y_) == 1 and x == x_)

        if is_correct:
            tail = word[1:]

            if tail:
                is_correct = function(cache, coordinates=(x_, y_), word=tail)

            return is_correct

    return is_correct


assert function(cache_, word='BEC') is False
assert function(cache_, word='SEAT')
assert function(cache_, word='TEA')
assert function(cache_, word='AGTAI') is False
assert function(cache_, word='CAGTAE')
assert function(cache_, word='EATG')
assert function(cache_, word='EASTG') is False
assert function(cache_, word='CAGTAI') is False








