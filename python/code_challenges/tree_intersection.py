def tree_intersection_(tree1, tree2):
    return set(tree1.pre_order()).intersection(set(tree2.pre_order()))


def tree_intersection(tree1, tree2):
    dict_ = {}
    dupes = set()
    for x in tree1.pre_order():
        dict_[x] = x
    for x in tree2.pre_order():
        if x in dict_:
            dupes.add(x)
    return dupes