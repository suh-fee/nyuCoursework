def most_frequent(lst):
    dict1 = {}
    max = 0
    for i in lst:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

        if dict1[i] > max:
            max = i

    return max

# a hash table could be used to inprove the runtime of this.
    # use i as keys, and find the index that has the most collisions

class OpenAddressingHashMap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    def __init__(self):
        self.capacity = 20
        self.size = 0
        self.table = [] * 20

    def __len__(self):
        return self.size

    def is_empty(self):
        if len(self) == 0:
            return True
        return False

    def __getitem__(self, item):
        pass
