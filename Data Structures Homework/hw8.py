import copy


class BinarySearchTreeMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value
            self.count = 0


    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None

        def num_children(self):
            count = 0
            if (self.left is not None):
                count += 1
            if (self.right is not None):
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None


    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0


    # raises exception if not found
    def __getitem__(self, key):
        node = self.subtree_find(self.root, key)
        if (node is None):
            raise KeyError(str(key) + " not found")
        else:
            return node.item.value

    # returns None if not found
    def subtree_find(self, subtree_root, key):
        curr = subtree_root
        while (curr is not None):
            if (curr.item.key == key):
                return curr
            elif (curr.item.key > key):
                curr = curr.left
            else:  # (curr.item.key < key)
                curr = curr.right
        return None


    # updates value if key already exists
    def __setitem__(self, key, value):
        node = self.subtree_find(self.root, key)
        if (node is None):
            self.subtree_insert(key, value)
        else:
            node.item.value = value

    # assumes key not in tree
    def subtree_insert(self, key, value=None):
        item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(item)
        if (self.is_empty()):
            self.root = new_node
            self.size = 1
        else:
            parent = self.root
            if(key < self.root.item.key):
                curr = self.root.left
                item.count += 1
            else:
                curr = self.root.right

            while (curr is not None):
                parent = curr
                if (key < curr.item.key):
                    curr = curr.left
                    item.count += 1
                else:
                    curr = curr.right

            if (key < parent.item.key):
                parent.left = new_node

            else:
                parent.right = new_node

            new_node.parent = parent
            self.size += 1


    #raises exception if key not in tree
    def __delitem__(self, key):
        if (self.subtree_find(self.root, key) is None):
            raise KeyError(str(key) + " is not found")
        else:
            val = self.subtree_delete(self.root, key)

        return val

    #assumes key is in tree + returns value associated
    def subtree_delete(self, node, key):
        node_to_delete = self.subtree_find(node, key)
        value = node_to_delete.item.value
        key = node_to_delete.item.key
        num_children = node_to_delete.num_children()

        if (node_to_delete is self.root):
            if (num_children == 0):
                self.root = None
                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                if (self.root.left is not None):
                    self.root = self.root.left
                else:
                    self.root = self.root.right
                self.root.parent = None
                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        else:
            if (num_children == 0):
                parent = node_to_delete.parent
                if (node_to_delete is parent.left):
                    parent.left = None
                else:
                    parent.right = None

                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                parent = node_to_delete.parent
                if(node_to_delete.left is not None):
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right

                child.parent = parent
                if (node_to_delete is parent.left):
                    parent.left = child
                else:
                    parent.right = child

                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        return key

    # assumes non empty subtree
    def subtree_max(self, curr_root):
        node = curr_root
        while (node.right is not None):
            node = node.right
        return node


    def inorder(self):
        for node in self.subtree_inorder(self.root):
            yield node.item.key

    def subtree_inorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)

    def __iter__(self):
        for node in self.inorder():
            yield (node.item.key, node.item.value)


    def preorder(self):
        for node in self.subtree_preorder(self.root):
            yield node

    def subtree_preorder(self, curr_root):
        if (curr_root is None):
            pass
        else:
            yield curr_root
            yield from self.subtree_preorder(curr_root.left)
            yield from self.subtree_preorder(curr_root.right)

    def get_ith_smallest(self, i):
        compare = i
        if i > self.size:
            raise IndexError('Out of range.')

        curr = self.root
        num = -1
        while curr != None:
            if (curr.item.count + 1) == compare:
                num = curr.item.key
            elif curr.item.count < compare:
                compare = compare - (curr.item.count + 1)
                curr = curr.right
            else:
                curr = curr.left

        return num

    def gen(self, i):
        yield self.inorder()

    def get_ith_smallest1(self, i):

        if i > self.size:
            raise IndexError('Out of range.')

        curr = self.root
        next = self.root.left

        if i == 1:
            while next != None:
                curr = curr.left
                next = next.left
            return curr.item.key

        tree = copy.deepcopy(self)

        val = ''

        for i in range(i):

            curr = tree.root
            next = tree.root.left
            while next != None:
                curr = curr.left
                next = next.left

            val = tree.__delitem__(curr.item.key)


        return val








# question 2
# a
def create_chain_bst(n):
    tree = BinarySearchTreeMap()
    for i in range(n, 0, -1): # runtime theta(n) bc for loop w input
        tree.subtree_insert(i) # runtime theta(n) bc subtree insert / theta(h)
    return tree # total theta (n ** 2)

# b
def add_items(bst, low, high):
    if low == high:
        bst.subtree_insert(low)
    else:
        middle = (high + low) // 2
        bst.subtree_insert(middle) # runtime of theta(n)
        add_items(bst, low, middle-1)
        add_items(bst, middle+1, high)

def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n) # will do it once for every number from 1 to n, so theta(n) on top of what happens inside
    return bst # theta(n**2)

# question 3

def restore_bst(prefix_list):
    tree = BinarySearchTreeMap()
    for i in prefix_list:
        tree.subtree_insert(i)
    return tree

# question 4



def find_min_abs_difference(bst):
    fin = []

    for i in bst.inorder():
        fin.append(i.item.key)

    compare = fin[0]
    mini = fin[-1]

    for i in range(len(fin)):
        if fin[i] != compare:
            if (fin[i] - fin[i-1]) < mini:
                mini = fin[i] - fin[i-1]

    return mini





#
# def main():
#     tree = create_complete_bst(7)
#     tree2 = create_chain_bst(7)
#
#     for i in tree:
#         print(i)
#
#     print('\n')
#     for i in tree2:
#         print(i)
#
# main()