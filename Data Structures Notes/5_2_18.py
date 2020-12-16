# min heap def

class ArrayMinHeap:
    class Item:
        def __init__(self, priority, value=None):
            self.priority = priority
            self.value = value

    def __init__(self):
        self.data = [None]

    def __len__(self):
        return len(self.data) - 1

    def is_empty(self):
        return len(self) == 0

    def left(self, i):
        return 2 * i

    def right(self, i):
        return (2 * i) + 1

    def parent(self, i):
        return i//2

    def has_left(self, i):
        return self.left(i) <= (len(self.data) - 1)

    def has_right(self, i):
        return self.right(i) <= (len(self.data) - 1)

    def min(self):
        if self.is_empty():
            raise Exception('Empty')
        item = self.data[1]
        return (item.priority, item.value)

    def insert(self, pri, val):
        new_item = ArrayMinHeap.Item(pri, val)
        self.data.append(new_item)
        self.fix_up(len(self.data) - 1)

    def swap(self, i1, i2):
        self.data[i1], self.data[i2] = self.data[i2], self.data[i1]

    def delete_min(self):
        if self.is_empty():
            raise Exception('Empty')
        # swap, pop, fix down (what the fuck does that mean kobe bryant)
        self.swap(1, len(self))
        min_item = self.data.pop()
        self.fix_down(1)
        return (min_item.priority, min_item.value)

    def fix_up(self, i):
        if i == 1:
            return
        parent = self.parent(i)
        if (self.data[i] < self.data[parent]):
            self.swap(i, parent)
            self.fix_up(parent)

    def fix_down(self, i):
        if(self.has_left(i)):
            left = self.left(i)
            smaller_child = left
            if self.has_right(i):
                right = self.right(i)
                if self.data[right] < self.data[left]:
                    smaller_child = right
            if self.data[i] > self.data[smaller_child]:
                self.swap(i, smaller_child)
                self.fix_down(smaller_child)


def heap_sort(lst):
    h = ArrayMinHeap()
    for elem in lst:
        h.insert(elem, None)
    res_lst = []
    while h.is_empty() == False:
        res_lst.append(h.delete_min())

    return res_lst


