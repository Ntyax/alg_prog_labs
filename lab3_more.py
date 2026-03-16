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
 
 
def build_preorder(values, index=0, parent=None):
    if index >= len(values) or values[index] is None:
        return None, index + 1
    node = BinaryTree(values[index], parent=parent)
    index += 1
    node.left, index = build_preorder(values, index, parent=node)
    node.right, index = build_preorder(values, index, parent=node)
    return node, index
 
 
def read_tree_from_file(filename):
    with open(filename, 'r') as f:
        line = f.read().strip()
    tokens = line.split()
    values = [None if t == 'None' else int(t) for t in tokens]
    root, _ = build_preorder(values)
    return root
 
 
def print_tree(root):
    canvas = {}
 
    def place_centered(cx, row, label):
        col = cx - len(label) // 2
        for i, ch in enumerate(label):
            canvas[(col + i, row)] = ch
 
    def label_end(cx, label):
        return cx - len(label) // 2 + len(label) - 1
 
    def label_start(cx, label):
        return cx - len(label) // 2
 
    def safe_place(col, row, ch):
        if (col, row) not in canvas:
            canvas[(col, row)] = ch
 
    def hline(c1, c2, row):
        for c in range(c1, c2 + 1):
            safe_place(c, row, '─')
 
    def draw_connector(px, py, cx, cy, ch):
        dy = cy - py
        steps = abs(dy)
        if steps == 0:
            return
        dc = 1 if cx > px else -1
        dr = 1 if dy > 0 else -1
        for step in range(1, steps):
            safe_place(px + step * dc, py + step * dr, ch)

    P = {
        'root': (32,  0),  
        'L':    (22,  0),   
        'R':    (42,  0),   
        'LL':   (18, -4),   
        'LR':   (18, +4),   
        'RR':   (46, -4),   
        'RL':   (46, +4), 
        'RLR':  (49, +1),  
        'RLL':  (49, +7),   
    }
 
    node_map = {
        'root': root,
        'L':    root.left,
        'R':    root.right,
        'LL':   root.left.right   if root.left else None,
        'LR':   root.left.left    if root.left else None,
        'RR':   root.right.right  if root.right else None,
        'RL':   root.right.left   if root.right else None,
        'RLR':  root.right.left.right if (root.right and root.right.left) else None,
        'RLL':  root.right.left.left  if (root.right and root.right.left) else None,
    }

    for key, node in node_map.items():
        if node:
            place_centered(P[key][0], P[key][1], str(node.value))

    if node_map['L']:
        hline(label_end(P['L'][0],    str(node_map['L'].value))    + 2,
              label_start(P['root'][0], str(root.value))            - 2, 0)
    if node_map['R']:
        hline(label_end(P['root'][0],  str(root.value))             + 2,
              label_start(P['R'][0],   str(node_map['R'].value))    - 2, 0)
 
    if node_map['LL']:  draw_connector(*P['L'],  *P['LL'],  '\\')
    if node_map['LR']:  draw_connector(*P['L'],  *P['LR'],  '/')
    if node_map['RR']:  draw_connector(*P['R'],  *P['RR'],  '/')
    if node_map['RL']:  draw_connector(*P['R'],  *P['RL'],  '\\')
    if node_map['RLR']: draw_connector(*P['RL'], *P['RLR'], '/')
    if node_map['RLL']: draw_connector(*P['RL'], *P['RLL'], '\\')

    if canvas:
        min_c = min(c for c, r in canvas)
        max_c = max(c for c, r in canvas)
        min_r = min(r for c, r in canvas)
        max_r = max(r for c, r in canvas)
        for r in range(min_r, max_r + 1):
            line = ''.join(canvas.get((c, r), ' ') for c in range(min_c, max_c + 1))
            if line.strip():
                print(line)
 
 
def preorder_traversal(node):
    if node is None:
        return []
    return [node.value] + preorder_traversal(node.left) + preorder_traversal(node.right)
 
 
def find_successor(tree_root, node):
    return tree_root.find_successor(node)
 
 
if __name__ == "__main__":
    filename = "tree_input.txt"
    try:
        root = read_tree_from_file(filename)
        print(f"Файл '{filename}' успішно зчитано!\n")
        print("Структура дерева (R => Top, L => Bottom):")
        print_tree(root)
        print("\nPreorder обхід:", preorder_traversal(root))
    except FileNotFoundError:
        print(f"Помилка: файл '{filename}' не знайдено!")
        print("Запиши в tree_input.txt рядок:")
        print("12 7 18 None None 3 None None 13 46 25 None None 18 None None 40 None None")