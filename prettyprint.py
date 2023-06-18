def pretty_print(tree):
    print("")
    pp = _pretty_print_strs(tree)
    for line in pp:
        print(line)

def _pretty_print_strs(tree):
    if tree.is_leaf():
        return ['+--- ' + tree._name.split()[0]]
    else:
        ltree = _pretty_print_strs(tree._left)
        rtree = _pretty_print_strs(tree._right)
        nltree = len(ltree)
        nrtree = len(rtree)
        adjusted = _adjust_left(ltree, 0, nltree) + ['|'] +  _adjust_right(rtree, 0, nrtree)
        return _shift(adjusted, 0, len(adjusted))

def _shift(strlist, i, n):
    if strlist == []:
        return []
    else:
        if i == n//2:
            sh_str = ['+---' + strlist[0]]
        else:
            sh_str = ['    ' + strlist[0]]

        return sh_str + _shift(strlist[1:], i+1, n)

def _adjust_left(L, i, n):
    if i == n:
        return []
    else:
        if i <= n//2:
            adj = ' '
        else:
            adj = '|'

        return [adj + L[i]] + _adjust_left(L, i+1, n)
        

def _adjust_right(L, i, n):
    if i == n:
        return []
    else:
        if i >= n//2:
            adj = ' '
        else:
            adj = '|'

        return [adj + L[i]] + _adjust_right(L, i+1, n)
        