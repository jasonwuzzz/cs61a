LAB_SOURCE_FILE = __file__



this_file = __file__

def skip_add(n):
    """ Takes a number n and returns n + n-2 + n-4 + n-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'skip_add',
    ...       ['While', 'For'])
    True
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + skip_add(n - 2)


def summation(n, term):

    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    if n == 1:
        return term(1)
    else:
        return term(n) + summation(n -1 , term)


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if 1 in (m, n):
        return 1
    else:
        return paths(m - 1, n) + paths(m, n - 1)


def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    For example, for n = 20125 and t = 3, we have that the subsequences are
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    and of these, the maxumum number is 225, so our answer is 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    # def helper(n, t):
    #     """
    #     Find all the subsequences of n at the length of t.
    #     """
    #     # Base Case 1: Return all the numbers in n
    #     if t == 1:
    #         return [int(i) for i in str(n)]
    #     # Base Case 2: n is a single digit or the length of n is t.
    #     elif n < 10 or len(str(n)) == t:
    #         return [n]
    #     # Recursive Case: Consider whether use the last digit or not
    #     else:
    #         # if use the last digit
    #         use_last = [x * 10 + n % 10 for x in helper(n // 10, t - 1)]
    #         not_use_last = helper(n // 10, t)
    #         return use_last + not_use_last    
    # # 0 is of length of 0
    # if t == 0:
    #     return 0
    # else:
    #     return max([max(helper(n, i)) for i in range(1, t + 1)]) 
    """Better version in Lecture 19 Q&A"""
    if t == 0 or n == 0:
      return 0 
    else:
      last_digit = n % 10
      rest = n // 10
      keep_last_digit = max_subseq(rest, t - 1) * 10 + last_digit
      drop_last_digit = max_subseq(rest, t)
      return max(keep_last_digit, drop_last_digit)


def add_chars(w1, w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.

    You may assume that w1 is a subsequence of w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    >>> from construct_check import check
    >>> # ban iteration and sets
    >>> check(LAB_SOURCE_FILE, 'add_chars',
    ...       ['For', 'While', 'Set', 'SetComp']) # Must use recursion
    True
    """
    def get_loc(char, w2, index=0):
        """helper function to find the location of  w1[0] in w2."""
        if char == w2[0]:
            return index
        else:
            return get_loc(char, w2[1:], index + 1)
    if w1 == "":
        return w2
    else:
        # get the add_chars without the first char in w1.
        sub_seq = add_chars(w1[1:], w2)
        # get rid of w1[0] in the sub_seq.
        index = get_loc(w1[0], w2)
        return sub_seq[:index] + sub_seq[index + 1:]
    # def add_chars(w1, w2):
    # """Tree recursion version in Lecture 12 Q&A."""
    # # Base Case
    # if w1 == "":
    #     return w2
    # # Consider the occurence of w1[0] in w2
    # elif w1[0] == w2[0]:
    #     return add_chars(w1[1:], w2[1:])
    # else:
    #     return w2[0] + add_chars(w1, w2[1:])
