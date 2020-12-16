
class ArrayQueue:
    INITIAL_CAPACITY = 5

    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.front_ind = 0
        self.number_of_elems = 0

    def __len__(self):
        return self.number_of_elems

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, item):
        if(self.number_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        end_ind = (self.front_ind + self.number_of_elems) % len(self.data)
        self.data[end_ind] = item
        self.number_of_elems += 1

    def dequeue(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.number_of_elems -= 1
        if (self.number_of_elems < (len(self.data) // 4)):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        old_ind = self.front_ind
        for new_ind in range(self.number_of_elems):
            new_data[new_ind] = self.data[old_ind]
            old_ind  = (old_ind + 1) % len(self.data)
        self.data = new_data
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
        if(self.is_empty()):
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
        if(curr_root is None):
            pass
        else:
            yield curr_root
            yield from self.subtree_preorder(curr_root.left)
            yield from self.subtree_preorder(curr_root.right)


    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_postorder(curr_root.left)
            yield from self.subtree_postorder(curr_root.right)
            yield curr_root


    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)


    def breadth_first(self):
        if (self.is_empty()):
            return
        line = ArrayQueue()
        line.enqueue(self.root)
        while (line.is_empty() == False):
            curr_node = line.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)

    def iterative_inorder(self):

        curr = self.root
        while curr != None:

            if curr.left == None:
                yield curr.data
                curr = curr.right

            else:

                next = curr.left

                while next.right != None and next.right != curr:
                    next = next.right

                if next.right == None:
                    next.right = curr
                    curr = curr.left

                else:
                    next.right = None
                    yield curr.data
                    curr = curr.right




    def __iter__(self):
        for node in self.postorder():
            yield node.data


# def main():
#
#
#     p1 = LinkedBinaryTree.Node(1)
#     p2 = LinkedBinaryTree.Node(6)
#     p3 = LinkedBinaryTree.Node(2, p1, p2)
#     p4 = LinkedBinaryTree.Node(4)
#     p5 = LinkedBinaryTree.Node(5, p3, p4)
#
#     binary_tree1 = LinkedBinaryTree(p5)
#
#
#     for item in binary_tree1.iterative_inorder():
#         print(item,  end=' ')
# main()