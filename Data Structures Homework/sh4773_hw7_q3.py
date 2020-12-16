

class EmptyTree(Exception):
    pass


class ArrayQueue:
    initial = 5

    def __init__(self):
        self.data = [None] * ArrayQueue.initial
        self.front_ind = 0
        self.num_elems = 0

    def __len__(self):
        return self.num_elems

    def is_empty(self):
        return self.num_elems == 0

    def enqueue(self, item):
        if self.num_elems == len(self.data):
            self.resize(len(self.data) * 2)
        end_ind = (self.front_ind + self.num_elems) % len(self.data)
        self.data[end_ind] = item
        self.num_elems += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue empty')
        val = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_elems -= 1
        if self.num_elems < (len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return val

    def first(self):
        if self.is_empty():
            raise Empty('Queue empty')
        return self.data[self.front_ind]

    def resize(self, new_size):
        old_data = self.data
        self.data = [None] * new_size
        old_ind = self.front_ind
        for new_ind in range(new_size):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0


class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def subtree_count(self, subtree_root):
        if (subtree_root is None):
            return 0
        else:
            left_count = self.subtree_count(subtree_root.left)
            right_count = self.subtree_count(subtree_root.right)
            return 1 + left_count + right_count

    def sum(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, subtree_root):
        if (subtree_root is None):
            return 0
        else:
            left_sum = self.subtree_sum(subtree_root.left)
            right_sum = self.subtree_sum(subtree_root.right)
            return subtree_root.data + left_sum + right_sum

    def height(self):
        if (self.is_empty()):
            raise Exception("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    def subtree_height(self, subtree_root):
        if ((subtree_root.left is None) and (subtree_root.right is None)):
            return 0
        elif ((subtree_root.left is not None) and (subtree_root.right is None)):
            return 1 + self.subtree_height(subtree_root.left)
        elif ((subtree_root.left is None) and (subtree_root.right is not None)):
            return 1 + self.subtree_height(subtree_root.right)
        else:
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)
            return 1 + max(left_height, right_height)

    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, curr_root):
        if (curr_root is None):
            pass
        else:
            yield curr_root
            yield from self.subtree_preorder(curr_root.left)
            yield from self.subtree_preorder(curr_root.right)

    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, curr_root):
        if (curr_root is None):
            pass
        else:
            yield from self.subtree_postorder(curr_root.left)
            yield from self.subtree_postorder(curr_root.right)
            yield curr_root

    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, curr_root):
        if (curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)

    def breadth_first(self):
        if (self.is_empty()):
            return
        line = ArrayQueue.ArrayQueue()
        line.enqueue(self.root)
        while (line.is_empty() == False):
            curr_node = line.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)

    def __iter__(self):
        for node in self.postorder():
            yield node.data

    def leaves_lst(self):
        if self.is_empty():
            raise Exception('Tree is empty')
        return [i for i in self.leaves_help(self.root)]

    def leaves_help(self, curr_root):
        if curr_root.left is None and curr_root.right is None:
            yield curr_root.data
        elif curr_root.left is None and curr_root.right is not None:
            yield from self.leaves_help(curr_root.right)
        elif curr_root.right is None and curr_root.left is not None:
            yield from self.leaves_help(curr_root.left)
        else:
            yield from self.leaves_help(curr_root.left)
            yield from self.leaves_help(curr_root.right)

    def iterative_inorder(self):
        cursor = self.root
        while cursor is not None:
            if cursor.left is None:
                yield cursor.data
                cursor = cursor.right
            else:
                bef = cursor.left
                while bef.right is not None and bef.right != cursor:
                    bef = bef.right
                if bef.right is None:
                    bef.right = cursor
                    cursor = cursor.left
                else:
                    bef.right = None
                    yield cursor.data
                    cursor = cursor.right



def balance_helper(subtree_root):

    if subtree_root.left == None and subtree_root.right == None:

        rightheight = 1
        leftheight = 1

    elif subtree_root.right == None:

        rightheight = 1
        leftheight = balance_helper(subtree_root.left) + 1

        if leftheight == False:
            return False

    elif subtree_root.left == None:

        leftheight = 1
        rightheight = balance_helper(subtree_root.right) + 1

        if rightheight == False:
            return False

    else:

        rightheight = balance_helper(subtree_root.right) + 1
        leftheight = balance_helper(subtree_root.left) + 1

        if rightheight == False or leftheight == False:
            return False

    difference = rightheight - leftheight

    if difference > 1 or difference < -1:
        return False

    elif rightheight > leftheight:
        return rightheight

    else:
        return leftheight


def is_height_balanced(bin_tree):
    height = balance_helper(bin_tree.root)

    if height == False:
        return False

    return True
