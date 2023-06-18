class Tree:
    def __init__(self, name=None):
        self._name = name
        self._left = None
        self._right = None
        self._ngrams = set()
    def get_ngrams(self):
        return self._ngrams
    def get_name(self):
        return self._name
    def is_leaf(self):
        return self._left is None and self._right is None
    def get_leaves(self):
        if self.is_leaf():
            return [self]
        else:
            left_leaves = self._left.get_leaves()
            right_leaves = self._right.get_leaves()
            return left_leaves + right_leaves
