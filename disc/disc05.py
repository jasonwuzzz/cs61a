# Question 1.1
def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(b) for b in branches(t)])

# Question 1.2
def max_path_sum(t):
    """Return the maximum path sum of the tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return label(t)
    else:
        return label(t) + max([max_path_sum(b) for b in branches(t)])

# Question 1.3
def square_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,
    ...                 [tree(2,
    ...                     [tree(3),
    ...                     tree(4)]),
    ...                 tree(5,
    ...                     [tree(6,
    ...                         [tree(7)]),
    ...                     tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
      4
        9
        16
      25
        36
          49
        64
    """
    if is_leaf(t):
        return tree(label(t) ** 2)
    else:
        return tree(label(t) ** 2, [square_tree(b) for b in branches(t)])

# Question 1.4
def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if is_leaf(t) and label(t) == x:
        return [x] 
    for b in branches(t):
        path = find_path(b, x)
        if path != None:
            return [label(t)] + path

# Question 2.2
def prune_binary(t, nums):
    """
    Input:
    t: A tree consisting of '0's and '1's.
    nums: a list of binary numbers, represented as a string.

    Output:
    A new tree that contains only the numbers in NUMS that exist in T, None vice versa.

    A binary number n exists t if there is some path from the root to leaf of t whose value are equal to n.
    >>> t = tree('1', [tree('0', [tree('0'), tree('1')]), tree('1', [tree('0')])])
    >>> print_tree(prune_binary(t, ['01', '110', '100']))
    1
      0
        0
      1
        0
    >>> print_tree(prune_binary(t, ['01', '100']))
    1
      0
        0
    >>> print_tree(prune_binary(t, ['01', '110']))
    1
      1
        0
    >>> print_tree(prune_binary(t, ['100', '110']))
    1
      0
        0
      1
        0
    """
    if is_leaf(t):
        if label(t) in nums:
            return t
        return None
    else:
        next_valid_nums = [num[1:] for num in nums if num[0] == label(t)]
        new_branches = []
        for b in branches(t):
            pruned_branch = prune_binary(b, next_valid_nums)
            if pruned_branch is not None:
                new_branches = new_branches + [pruned_branch]
        if not new_branches:
            return None
    return tree(label(t), new_branches)


# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])