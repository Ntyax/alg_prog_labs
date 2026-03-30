class Node:
    def __init__(self, value, priority, color="RED"):
        self.value = value
        self.priority = priority
        self.color = color
        self.left = None
        self.right = None
        self.parent = None
 
class RedBlackPriorityQueue:
    def __init__(self):
        self.NIL = Node(None, float('+inf'), color="BLACK")
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.NIL.parent = self.NIL
        self.root = self.NIL

 
    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
 
    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is self.NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
 
    def _fix_insert(self, k):
        while k.parent.color == "RED":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._rotate_right(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self._rotate_left(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._rotate_left(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self._rotate_right(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "BLACK"

    def insert(self, value, priority):
        new_node = Node(value, priority)
        new_node.left = self.NIL
        new_node.right = self.NIL

        y = self.NIL
        x = self.root
 
        while x != self.NIL:
            y = x
            if new_node.priority < x.priority:
                x = x.left
            else:
                x = x.right
 
        new_node.parent = y
        if y is self.NIL:
            self.root = new_node
        elif new_node.priority < y.priority:
            y.left = new_node
        else:
            y.right = new_node
 
        if new_node.parent is self.NIL:
            new_node.color = "BLACK"
            return
 
        if new_node.parent.parent is self.NIL:
            return
 
        self._fix_insert(new_node)

    def extract_max(self):
        if self.root is self.NIL:
            raise IndexError("Черга порожня")
 
        node = self.root
        while node.left != self.NIL:
            node = node.left
 
        res_value = (node.value, node.priority)
        self._delete_node(node)
        return res_value

    def peek(self):
        if self.root is self.NIL:
            raise IndexError("Черга порожня")
        node = self.root
        while node.left != self.NIL:
            node = node.left
        return (node.value, node.priority)

    def _delete_node(self, z):
        y = z
        y_original_color = y.color
 
        if z.left is self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right is self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent is z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
 
        if y_original_color == "BLACK":
            self._fix_delete(x)
 
    def _transplant(self, u, v):
        if u.parent is self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
 
    def _minimum(self, x):
        while x.left != self.NIL:
            x = x.left
        return x
 
    def _fix_delete(self, x):
        while x is not self.root and x.color == "BLACK":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self._rotate_left(x.parent)
                    w = x.parent.right
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self._rotate_right(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self._rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self._rotate_right(x.parent)
                    w = x.parent.left
                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self._rotate_left(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self._rotate_right(x.parent)
                    x = self.root
        x.color = "BLACK"

    def peek_all(self):
        elements = []
        self._inorder_helper(self.root, elements)
        return elements
 
    def _inorder_helper(self, node, elements):
        if node != self.NIL:
            self._inorder_helper(node.left, elements)
            elements.append((node.value, node.priority))
            self._inorder_helper(node.right, elements)
 
pq = RedBlackPriorityQueue()
pq.insert("Завдання А", 10)
pq.insert("Завдання Б", 20)
pq.insert("Завдання В", 15)
pq.insert("Критичний баг", 1)
 
print("Вміст черги (від вищого до нижчого пріоритету):", pq.peek_all())
print("peek():", pq.peek())
print("extract_max():", pq.extract_max())
print("extract_max():", pq.extract_max())
print("Після двох видалень:", pq.peek_all())