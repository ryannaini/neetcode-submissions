class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map the key to the Nodes 

        self.left, self.right = Node(0, 0), Node(0, 0) # Default LRU and MRU

        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next

        prev.next, nxt.prev = nxt, prev


    # insert from right 
    def insert(self, node):
        prev, nxt = self.right.prev, self.right

        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev 
        

    def get(self, key: int) -> int:
        if key in self.cache:
            # TODO: update most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove from the LRU and delete the LRU from the CACHE / HashMap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key] # del deletes from the hashmap but needs the key

