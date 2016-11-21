def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Put runtime here:
    -----------------
    [     O(1)          ]


    """

    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Put runtime here:
    -----------------
    [       O(n)        ]

    """

    if "hippo" in animals or "platpypus" in animals:      #n+n
        return True
    else:
        return False


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [       O(n^2)        ]

    """

    result = []

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later
    s = set(numbers)                      #n

    for x in s:                           #n
        if -x in s:                       #n
            result.append([-x, x])        #1

    return result                         #So: n+n*n (and the multiplte dominates)


def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [        O(n^2)       ]

    """

    result = []                                 #1

    for x in numbers:                            #n
        for y in numbers:                        #n
            if x == -y:                          # <<< Not 100% sure this won't compound with another n, and it occurs below too!
                result.append((x, y))            #1
    return result                                


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    Put runtime here:
    -----------------
    [        O(n^3)       ]

    """

    result = []

    for x in numbers:                                   #n
        for y in numbers:                               #n
            if x == -y and (y, x) not in result:        #n
                result.append((x, y))                   #1
    return result
