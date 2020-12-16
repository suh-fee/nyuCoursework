# question 3

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
        try:
            return curr_bucket[key]
        except Exception:
            return curr_bucket.value

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        if self.table[i] == None:
            self.table[i] = UnsortedArrayMap().Item(key, value)
        elif type(self.table[i]) != "class '__main__.UnsortedArrayMap'>":
            prev_item = self.table[i]
            self.table[i] = UnsortedArrayMap()
            self.table[i][prev_item.key] = prev_item.value
        if type(self.table[i]) == "class '__main__.UnsortedArrayMap'>":
            old_size = len(self.table[i])
            self.table[i][key] = value
            new_size = len(self.table[i])
            if (new_size > old_size):
                self.n += 1
            if (self.n > self.N):
                self.rehash(2 * self.N)

    def __delitem__(self, key):
        i = self.hash_function(key)
        curr = self.table[i]

        if curr == None:
            raise KeyError("Key Error: " + str(key))

        if type(curr) == "class '__main__.UnsortedArrayMap'>":
            del curr[key]

            if len(curr) == 1:

                for leftover_key in curr:
                    leftover = leftover_key

                curr = UnsortedArrayMap().Item(leftover, curr[leftover])

            self.n -= 1

            if (curr.is_empty()):
                self.table[i] = None

            if (self.n < self.N // 4):
                self.rehash(self.N // 2)
        else:
            curr.key = None
            curr.value = None

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