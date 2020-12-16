class Empty(Exception):
    pass


class ArrayQueue:
    INITIAL_CAPACITY = 10
    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = 0
    def __len__(self):
        return self.num_of_elems
    def is_empty(self):
        return (self.num_of_elems == 0)
    def enqueue(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1
    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value
    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front_ind]
    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
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
        if(self.is_empty()):
            raise Exception("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    def subtree_height(self, subtree_root):
        if (subtree_root.left is None and subtree_root.right is None):
            return 0
        elif (subtree_root.left is not None):
            return 1 + self.subtree_height(subtree_root.left)
        elif (subtree_root.right is not None):
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


    def __iter__(self):
        for node in self.postorder():
            yield node.data


def level_list(root, level):

    if level == 0:
        return [root.data]
    else:
        left = []
        right = []

        if root.left != None:
            left = level_list(root.left, level-1)

        if root.right != None:
            right = level_list(root.right, level-1)

        left.extend(right)
        return left

    # def helper(root, level, list):
    #     if level == 0:
    #         list.append(root.data)
    #     else:
    #         if root.left != None:
    #             helper(root.left, level-1, list)
    #         if root.right != None:
    #             helper(root.right, level-1, list)
    # fin = []
    # helper(root, level, fin)
    # return fin


# def main():
#     tree = LinkedBinaryTree()
#     tree.root = LinkedBinaryTree.Node(1)
#     left1 = LinkedBinaryTree.Node(2)
#     right1 = LinkedBinaryTree.Node(5)
#
#     tree.root.left = left1
#     tree.root.right = right1
#
#     left2 = LinkedBinaryTree.Node(4)
#     right2 = LinkedBinaryTree.Node(5)
#
#     left1.left = left2
#     left1.right = right2
#
#     right21 = LinkedBinaryTree.Node(9)
#     right1.right = right21
#
#     left3 = LinkedBinaryTree.Node(7)
#     right3 = LinkedBinaryTree.Node(6)
#
#     left2.left = left3
#     left2.right = right3
#
#     right4 = LinkedBinaryTree.Node(10)
#     right2.right = right4
#
#     yes = LinkedBinaryTree.Node(19)
#     yer = LinkedBinaryTree.Node(13)
#
#     right21.left = yes
#     right21.right = yer
#
#     print(level_list(tree.root, 3))
#
# main()

# last q

import random

class UnsortedArrayMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value


    def __init__(self):
        self.table = []

    def __len__(self):
        return len(self.table)

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        for item in self.table:
            if key == item.key:
                return item.value
        raise KeyError("Key Error: " + str(key))

    def __setitem__(self, key, value):
        for item in self.table:
            if key == item.key:
                item.value = value
                return
        self.table.append(UnsortedArrayMap.Item(key, value))

    def __delitem__(self, key):
        for j in range(len(self.table)):
            if key == self.table[j].key:
                self.table.pop(j)
                return
        raise KeyError("Key Error: " + str(key))

    def __iter__(self):
        for item in self.table:
            yield item.key


class ChainingHashTableMap:

    def __init__(self, N=64, p=40206835204840513073):
        self.N = N
        self.table = [None] * self.N
        self.n = 0
        self.p = p
        self.a = random.randrange(1, self.p - 1)
        self.b = random.randrange(0, self.p - 1)

    def hash_function(self, k):
        return ((self.a * hash(k) + self.b) % self.p) % self.N

    def __len__(self):
        return self.n

    def __getitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        return curr_bucket[key]

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        if self.table[i] is None:
            self.table[i] = UnsortedArrayMap()
        old_size = len(self.table[i])
        self.table[i][key] = value
        new_size = len(self.table[i])
        if (new_size > old_size):
            self.n += 1
        if (self.n > self.N):
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        del curr_bucket[key]
        self.n -= 1
        if (curr_bucket.is_empty()):
            self.table[i] = None
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)

    def __iter__(self):
        for curr_bucket in self.table:
            if (curr_bucket is not None):
                for key in curr_bucket:
                    yield key

    def rehash(self, new_size):
        old = []
        for key in self:
            value = self[key]
            old.append((key, value))
        self.table = [None] * new_size
        self.n = 0
        self.N = new_size
        for (key, value) in old:
            self[key] = value


class Playlist:
    def __init__(self):
        self.playlist = ChainingHashTableMap()
        self.before = None
        self.start = None

    def add_song(self, new_song_name):

        if self.before != None:
            self.playlist[self.before][1] = new_song_name
        else:
            self.start = new_song_name

        self.playlist[new_song_name] = [new_song_name, None]
        self.before = new_song_name

    def add_song_after(self, song_name, new_song_name):
        latter = self.playlist[song_name][1]
        self.playlist[song_name][1] = new_song_name
        self.playlist[new_song_name] = [new_song_name, latter]


    def play_song(self, song_name):
        print(self.playlist[song_name][0])

    def play_list(self):
        curr = self.start
        while curr != None:
            self.play_song(curr)
            next1 = self.playlist[curr][1]
            curr = next1



def main1():
    pl = Playlist()
    pl.add_song("Feel It Still")

    pl.add_song("Perfect")

    pl.add_song("Havana")

    pl.add_song_after("Perfect", "Thunder")

    pl.add_song_after("Feel It Still", "Something Just Like This")
    pl.play_list()

class TrafficLight:
    def __init__(self, color):
        self.color = color
        self.num_cars = 0

    def add_car(self, val):
        if self.color == 'Red':
            self.num_cars += val

    def change(self, color):
        self.color = color
        if color == 'Green':
            self.num_cars = 0

    def __repr__(self):
        return 'Color: ' + self.color + ' Num cars: ' + str(self.num_cars)

    def __add__(self, other):
        fin = self.num_cars + other.num_cars
        new = TrafficLight('Red')
        new.num_cars = fin
        return new


#
# light1 = TrafficLight('Red')
# light2 = TrafficLight('Red')
# light1.add_car(12)
# light2.add_car(8)
# print(light1 + light2)
# print(light1)

class ArrayMinHeap:
    class Item:
        def __init__(self, priority, value=None):
            self.priority = priority
            self.value = value

        def __lt__(self, other):
            return self.priority < other.priority


    def __init__(self, priorities_lst=None, values_lst = None):
        self.data = [None]

    def __len__(self):
        return len(self.data) - 1

    def is_empty(self):
        return len(self) == 0


    def left(self, j):
        return 2*j

    def right(self, j):
        return 2*j+1

    def parent(self, j):
        return j // 2


    def has_left(self, j):
        return self.left(j) <= len(self.data) - 1

    def has_right(self, j):
        return self.right(j) <= len(self.data) - 1


    def min(self):
        if self.is_empty():
            raise Exception("Priority queue is empty.")
        item = self.data[1]
        return (item.priority, item.value)


    def insert(self, priority, value=None):
        self.data.append(ArrayMinHeap.Item(priority, value))
        self.fix_up(len(self.data) - 1)


    def delete_min(self):
        if self.is_empty():
            raise Exception("Priority queue is empty.")
        self.swap(1, len(self.data) - 1)
        item = self.data.pop()
        if (not self.is_empty()):
            self.fix_down(1)
        return (item.priority, item.value)

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def fix_up(self, j):
        if(j == 1):
            return
        else:
            parent_ind = self.parent(j)
            if (self.data[j] < self.data[parent_ind]):
                self.swap(j, parent_ind)
                self.fix_up(parent_ind)

    def fix_down(self, j):
        if (self.has_left(j)):
            left = self.left(j)
            small_child = left
            if (self.has_right(j)):
                right = self.right(j)
                if self.data[right] < self.data[left]:
                    small_child = right
            if self.data[small_child] < self.data[j]:
                self.swap(j, small_child)
                self.fix_down(small_child)

    def find_less_than_or_equal(self,k):
        start = 1
        list1 = []
        self.helper(k,1,list1)
        return list1

    def helper(self, max, index, list):
        if self.data[index].priority == max:
            list.append(self.data[index].priority)
        elif self.data[index].priority < max:
            list.append(self.data[index].priority)
            if self.has_left(index):
                self.helper(max, self.left(index), list)
            if self.has_right(index):
                self.helper(max, self.right(index), list)


class Empty(Exception):
    pass


class ArrayDeque:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.front_ind = 0
        self.data = [None] * ArrayDeque.INITIAL_CAPACITY
        self.num_of_elems = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

    def add_first(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * self.num_of_elems)
        first = (self.front_ind - 1) % len(self.data)
        self.data[first] = elem
        self.front_ind = first
        self.num_of_elems += 1

    def add_last(self, e):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * self.num_of_elems)
        back = (self.front_ind + self.num_of_elems) % (len(self.data))
        self.data[back] = elem
        self.num_of_elems += 1

    def delete_first(self):
        if (self.is_empty()):
            raise Empty("Deque is empty")
        val = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % (len(self.data))
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return val

    def delete_last(self):
        if (self.is_empty()):
            raise Empty("Deque is empty")
        back_ind = (self.front_ind + self.num_of_elems - 1) % (len(self.data))
        val = self.data[back_ind]
        self.data[back_ind] = None
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return val

    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.data[self.front_ind]

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.data[(self.front_ind + self.num_of_elems - 1) % (len(self.data))]

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
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
        if(self.is_empty()):
            raise Exception("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    def subtree_height(self, subtree_root):
        if (subtree_root.left is None and subtree_root.right is None):
            return 0
        elif (subtree_root.left is not None):
            return 1 + self.subtree_height(subtree_root.left)
        elif (subtree_root.right is not None):
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


    def __iter__(self):
        for node in self.postorder():
            yield node.data




def main():
    heap = ArrayMinHeap()
    list1 = [1,7,3,11,15,5,9,19,13,17]
    for i in list1:
        heap.insert(i)
    print(heap.find_less_than_or_equal(11))

def k_largest_elements(lst, k):
    heap = ArrayMinHeap()
    max = 0
    fin = []

    for i in lst:
        if i > max:
            max = i

    max += 1

    for i in lst:
        heap.insert((max-i), i)

    for i in range(k):
        fin.append(heap.delete_min()[1])

    return fin

# print(k_largest_elements([3,9,2,7,1,7,1,3], 4))


def av(tree):
    counter = 0
    sum = 0
    sum, counter = helper(tree.root, sum, counter)
    return sum/counter

def helper(node, sum, counter):

    fin = sum
    count = counter
    fin += node.data
    count += 1

    if node.left != None:
        var1, var2 = helper(node.left, sum, counter)
        fin += var1
        count += var2

    if node.right != None:
        var1, var2 = helper(node.right, sum, counter)
        fin += var1
        count += var2

    return fin,count

def lowest(node):
    if node.left == None and node.right == None:
        return node.data
    compare = node.data

    if node.left != None:
        if compare > lowest(node.left):
            compare = lowest(node.left)

    if node.right != None:
        if compare > lowest(node.right):
            compare = lowest(node.right)

    return compare



def main():
    tree = LinkedBinaryTree()
    root = LinkedBinaryTree.Node(7)
    kid1 = LinkedBinaryTree.Node(2)
    kid2 = LinkedBinaryTree.Node(3)
    kid4 = LinkedBinaryTree.Node(4)
    kid5 = LinkedBinaryTree.Node(1)
    root.left = kid1
    root.right = kid2
    kid1.left = kid4
    kid1.right = kid5
    tree.root = root
    print(compare)
main()