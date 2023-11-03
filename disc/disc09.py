class A():
    def __init__(self, x):
        self.x = x
    def __repr__(self):
         return self.x
    def __str__(self):
         return self.x * 2

class B():
    def __init__(self):
         print("boo!")
         self.a = []
    def add_a(self, a):
         self.a.append(a)
    def __repr__(self):
         print(len(self.a))
         ret = ""
         for a in self.a:
             ret += str(a)
         return ret


def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if lnk is Link.empty:
        return 0
    else:
        return lnk.first + sum_nums(lnk.rest)


def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Note: you might not need all lines in this skeleton code
    mul = 1
    new_lst = []
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link.empty
        mul *= lnk.first
        new_lst.append(lnk.rest)
    return Link(mul, multiply_lnks(new_lst))



def flip_two(lnk):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if lnk is Link.empty or lnk.rest is Link.empty:
        pass
    else:
        lnk.first, lnk.rest.first = lnk.rest.first, lnk.first
        flip_two(lnk.rest.rest)


def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """

    while link is not Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest


def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    f = lambda x: x + 1 if x % 2 != 0 else x
    map_tree(t, f)
        

def square_tree(t):
    """Mutates a Tree t by squaring all its elements."""
    f = lambda x: x ** 2
    map_tree(t, f) 


def map_tree(t, map):
    t.label = map(t.label)
    for b in t.branches:
        map_tree(b, map)


def find_paths(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """

    paths = []
    if t.label == entry:
        return [[t.label]]
    for b in t.branches:
        if find_paths(b, entry):
            paths += [[t.label] + path for path in find_paths(b ,entry)]
    return paths


def combine_tree(t1, t2, combiner):
    """
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> mul = lambda x, y: x * y
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    label = combiner(t1.label, t2.label)
    branches = []
    for b1, b2 in zip(t1.branches, t2.branches):
        branches.append(combine_tree(b1, b2, combiner))
    return Tree(label, branches)
        

def alt_tree_map(t, map_fn):
   """
   >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
   >>> negate = lambda x: -x
   >>> alt_tree_map(t, negate)
   Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
   >>> s = Tree(2, [Tree(3)])
   >>> alt_tree_map(s, negate)
   Tree(-2, [Tree(3)])
   """
   t.label = map_fn(t.label)
   for b in t.branches:
       for g in b.branches:
           alt_tree_map(g, map_fn)
   return t
