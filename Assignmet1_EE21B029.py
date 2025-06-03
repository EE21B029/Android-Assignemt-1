#Least Recently used should be removed or to add a new one

from collections import OrderedDict

class LRU:
    def __init__(self, size):
        self.storage = OrderedDict()   #used to track the order
        self.size = size              # Max items allowed

    def get(self, key):
        if key not in self.storage:
            return -1
        self.storage.move_to_end(key)    #as its used recently its pushed to the end
        return self.storage[key]

    def put(self, key, value):
        if key in self.storage:
            self.storage.move_to_end(key)
        self.storage[key] = value

        if len(self.storage) > self.size:
            self.storage.popitem(last=False)     #we pop the first item as its least used.
