class Hashtable:
    
    def __init__(self):
        self.table = [None] * 256

    def hash(self, key):
        index = 0
        for char in key:
            index += ord(char)
        return index % 256

    def set(self, key, value):
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, pair in enumerate(self.table[index]):
                if pair[0] == key:
                    self.table[index][i] = (key, value)
                    break
            else:
                self.table[index].append((key, value))

    def get(self, key):
        index = self.hash(key)
        if self.table[index] is None:
            return None
        else:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
            else:
                return None

    def has(self, key):
        index = self.hash(key)
        if self.table[index] is None:
            return False
        else:
            for pair in self.table[index]:
                if pair[0] == key:
                    return True
            else:
                return False

    def keys(self):
        keys = []
        for pairs in self.table:
            if pairs is None:
                continue
            else:
                for pair in pairs:
                    keys.append(pair[0])
        return keys
