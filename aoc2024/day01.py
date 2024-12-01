with open('../inputs/day01.txt', 'r') as file:
    _left_numbers = []
    _right_numbers = []
    
    data = file.read()
    for line in data.split('\n'):
        left, right = line.split()  # Split on whitespace
        _left_numbers.append(int(left))
        _right_numbers.append(int(right))

_left_numbers.sort()
_right_numbers.sort()

left_numbers = _left_numbers
right_numbers = _right_numbers

print(sum(abs(left - right) for left, right in zip(left_numbers, right_numbers)))

from collections import Counter

lookup = Counter(right_numbers)

print(sum(lookup[left] * left for left in left_numbers))
