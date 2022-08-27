
class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [[] for i in range(self.max)]

    def get_hash(self,key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % self.max
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))

    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0]== key:
                return element[1]
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
    

h = HashTable()
h['march 6'] =302
h['march 11'] =76

del h['march 11']

print(h.arr)
