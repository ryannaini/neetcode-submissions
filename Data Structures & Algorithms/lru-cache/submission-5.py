class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None 


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left, self.right = Node(0,0), Node(0,0)
        
        self.cache = {}

        ## First Thing I forgot, setting the Nodes to be pointing to eachother 
        self.left.next, self.right.prev = self.right, self.left

    ## Second Thing I forgot, setting self as an input parameter, and node is an instance
    ## of a class therefore you don't use capitalization    
    def remove(self, node):
        nxt = node.next
        prev = node.prev

        prev.next = nxt
        nxt.prev = prev

    ## Third Thing, did not nearly understand insert enough
    def insert(self, node):
        prev, nxt = self.right.prev, self.right

        prev.next = nxt.prev = node

        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        ## We need to return the value but also remove from the cache then insert in the front
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

      
    def put(self, key: int, value: int) -> None:
        ## Fourth Thing, whenever key is in cache we need to remove and insert in the front
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            ## Fifth Thing, didn't handle this right
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        

