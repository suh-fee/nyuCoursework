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

    def find_less_than_or_equal_to(self, k):
        if self.is_empty():
            raise Exception("Priority queue is empty.")

        # lst1 = []
        # index = 0
        # height = -1
        #
        # lst1.append(self.data[index].priority)
        # index += 1
        # height += 1
        #
        # while self.data[index + (2**height)].priority <= k:
        #     lst1.append(self.data[index].priority)
        #     index += 1
        #
        # return lst1

        lst1 = []
        self.find_less_help(k, 1, lst1)
        return lst1


    def find_less_help(self, max, curr, list):

        if self.data[curr].priority > max:
            return

        list.append(self.data[curr].priority)

        if (self.has_left(curr)):
            left = self.left(curr)

            self.find_less_help(max, left, list)


            if (self.has_right(curr)):
                right = self.right(curr)

                self.find_less_help(max, right, list)


que = ArrayMinHeap()
counter = 5
for i in range(5):
    que.insert(i, counter)
    counter += 1

print(que.find_less_than_or_equal_to(3))




class FIFOQ:
    def __init__(self):
        self.que = ArrayMinHeap()
        self.counter = 1

    def enqueue(self, val):


        self.que.insert(self.counter, val)
        self.counter += 1



    def dequeue(self):
        item = self.que.delete_min()
        return item[1]

    def first(self):
        item = self.que.min()
        return item[1]

    def __len__(self):
        return len(self.que)

    def is_empty(self):
        return self.que.is_empty()


