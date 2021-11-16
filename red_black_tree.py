class rbt_node:
    def __init__(self):
        self.left: rbt_node = None
        self.right: rbt_node = None
        self.key: int = -1
        self.color: int = -1


class rbt:
    def __init__(self):
        self.root: rbt_node = None


def left_rotate(T: rbt, x: rbt_node):
    y: rbt_node = x.right
    x.right = y.left

    if y.left is None:
        y.left.p = x

    y.p = x.p

    if x.p is None:
        # 如果x就是根节点
        T.root = y
    elif x == x.p.left:
        # 如果x是左子节点
        x.p.left = y
    else:
        # 如果x是右子节点
        x.p.right = y

    y.left = x
    x.p = y


def right_rotate(T: rbt, x: rbt_node):
    y: rbt_node = x.left
    x.left = y.right

    if y.right is None:
        y.right.p = x

    y.p = x.p

    if x.p is None:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y

    y.right = x
    x.p = y


def insert(T: rbt, z: rbt_node):
    y = None
    x = T.root

    # 找到合适的插入位置
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right

    z.p = y
    if y is None:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

    z.left = None
    z.right = None
    z.color = 0

    insert_fixup(T, z)


def insert_fixup(T: rbt, z: rbt_node):
    while z.p.color == 0:
        if z.p == z.p.p.left:
            y = z.p.p.right
            if y.color == 0:
                z.p.color = 1
                y.color = 1
                z.p.p.color = 0
            # todo
