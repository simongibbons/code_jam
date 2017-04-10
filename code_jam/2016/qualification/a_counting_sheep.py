def solution(n):
    """
    >>> solution(0)
    'INSOMNIA'
    >>> solution(1)
    10
    >>> solution(2)
    90
    >>> solution(11)
    110
    >>> solution(1692)
    5076
    >>> solution(-1)
    -10
    """
    if n == 0:
        return 'INSOMNIA'

    result = n
    seen = set()
    while True:
        seen.update(int_to_list(result))
        if seen == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}:
            return result
        result += n


def int_to_list(n):
    """
    >>> int_to_list(1234)
    [1, 2, 3, 4]
    >>> int_to_list(0)
    [0]
    >>> int_to_list(-2)
    [2]
    """
    if n == 0:
        return [0]

    n = abs(n)

    result = []
    while n > 0:
        result.append(n % 10)
        n /= 10
    return result[::-1]


def main():
    num_cases = input()
    for i in xrange(1, num_cases + 1):
        x = input()
        result = solution(x)
        print "Case #{}: {}".format(i, result)


if __name__ == '__main__':
    main()
