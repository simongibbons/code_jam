def flip_pancakes(pancakes, position, flipper_size):
    """
    >>> "".join(flip_pancakes(list("---+"), 0, 4))
    '+++-'
    """
    if position < 0 or position > len(pancakes) - flipper_size:
        raise ValueError("Cannot Do this flip")

    result = pancakes[:]
    for i in xrange(position, position + flipper_size):
        result[i] = '+' if result[i] == '-' else '-'
    return result


def solution(pancakes, flipper_size):
    """
    >>> solution("---+-++-", 3)
    3
    >>> solution("+++++", 4)
    0
    >>> solution("-+-+-", 4)
    'IMPOSSIBLE'
    """
    pancakes = list(pancakes)

    flips_needed = 0
    for i in xrange(len(pancakes) - flipper_size + 1):
        if pancakes[i] != '+':
            flips_needed += 1
            pancakes = flip_pancakes(pancakes, i, flipper_size)
    if all(pancake == '+' for pancake in pancakes):
        return flips_needed
    else:
        return "IMPOSSIBLE"


def main():
    num_cases = input()
    for i in xrange(1, num_cases + 1):
        pancakes, flipper_size = raw_input().split()
        num_flips = solution(pancakes, int(flipper_size))
        print "Case #{}: {}".format(i, num_flips)


if __name__ == '__main__':
    main()
