
import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()


class ArrayQueue:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data_arr = make_array(ArrayQueue.INITIAL_CAPACITY)
        self.n = 0
        self.front_ind = None

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, item):
        if(self.n == len(self.data_arr)):
            self.resize(2 * len(self.data_arr))
        if(self.is_empty()):
            self.data_arr[0] = item
            self.front_ind = 0
            self.n = 1
        else:
            back_ind = (self.front_ind + self.n) % len(self.data_arr)
            self.data_arr[back_ind] = item
            self.n += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data_arr)
        self.n -= 1
        if(self.n == 0):
            self.front_ind = None
        if((self.n < len(self.data_arr) // 4) and  (len(self.data_arr) > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(len(self.data_arr) // 2)
        return value

    def first(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        return self.data_arr[self.front_ind]

    def resize(self, new_size):
        old_data = self.data_arr
        new_data = make_array(new_size)
        old_ind = self.front_ind
        for new_ind in range(self.n):
            new_data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.data_arr = new_data
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
        self.size = self.count_nodes()

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0


    def count_nodes(self):
        def subtree_count(root):
            if (root is None):
                return 0
            else:
                left_count = subtree_count(root.left)
                right_count = subtree_count(root.right)
                return 1 + left_count + right_count

        return subtree_count(self.root)


    def sum(self):
        def subtree_sum(root):
            if (root is None):
                return 0
            else:
                left_sum = subtree_sum(root.left)
                right_sum = subtree_sum(root.right)
                return root.data + left_sum + right_sum

        return subtree_sum(self.root)


    def height(self):
        def subtree_height(root):
            if (root.left is None and root.right is None):
                return 0
            elif (root.left is None):
                return 1 + subtree_height(root.right)
            elif (root.right is None):
                return 1 + subtree_height(root.left)
            else:
                left_height = subtree_height(root.left)
                right_height = subtree_height(root.right)
                return 1 + max(left_height, right_height)

        if(self.is_empty()):
            raise Exception("Tree is empty")
        return subtree_height(self.root)


    def preorder(self):
        def subtree_preorder(root):
            if (root is None):
                pass
            else:
                yield root
                yield from subtree_preorder(root.left)
                yield from subtree_preorder(root.right)

        yield from subtree_preorder(self.root)


    def postorder(self):
        def subtree_postorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_postorder(root.left)
                yield from subtree_postorder(root.right)
                yield root

        yield from subtree_postorder(self.root)


    def inorder(self):
        def subtree_inorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)


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

    def __iter__(self):
        for node in self.breadth_first():
            yield node.data





def main():
    str1 = "* 2 + - 15 6 4"
    print(str1)
    tree = create_expression_tree(str1)
    for i in tree.preorder():
        print(str(i.data) + " ", end="")
    print()

    print("2 15 6 - 4 + *")
    print(prefix_to_postfix(str1))
    print(create_expression_tree(""));
    return



def create_expression_tree(prefix_exp_str):
    def create_expression_tree_helper(prefix_str,start_pos):
        if prefix_str[start_pos].isdigit():
            return (LinkedBinaryTree.Node(int(prefix_str[start_pos])),1);
        else:
            left=create_expression_tree_helper(prefix_str,start_pos+1);
            right=create_expression_tree_helper(prefix_str,start_pos+left[1]+1)
            sub_root=LinkedBinaryTree.Node(prefix_str[start_pos],left[0],right[0]);
            return (sub_root,(left[1]+right[1]+1));
    prefix_exp_str=prefix_exp_str.split(" ");
    return LinkedBinaryTree(create_expression_tree_helper(prefix_exp_str,0)[0]);
def prefix_to_postfix(prefix_exp_str):
    return_str=""
    for item in create_expression_tree(prefix_exp_str).postorder():
        return_str+=str(item.data)+" ";
    return return_str.rstrip(" ");

main()