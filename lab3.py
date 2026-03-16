class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self._value = value
        self._left = left
        self._right = right
        self._parent = parent

    @property
    def value(self):
        return self._value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        self._parent = node

    def find_successor(self, node):
        if node.right is not None:
            return self._get_min(node.right)
        current = node
        parent = current.parent
        while parent is not None and current == parent.right:
            current = parent
            parent = parent.parent

        return parent

    def _get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current