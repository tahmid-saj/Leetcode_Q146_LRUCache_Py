class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {}
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.lru: return -1
        if key in self.lru:
            moveNode = self.lru[key]
            self.remove(moveNode)
            self.add(moveNode)
            return moveNode.val

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            node = self.lru[key]
            self.remove(node)

        newNode = ListNode(key, value)
        self.lru[key] = newNode
        self.add(newNode)
        
        if len(self.lru) > self.capacity:
            delNode = self.head.next
            self.remove(delNode)
            del self.lru[delNode.key]
        
    def remove(self, node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def add(self, node):
        prevNode, nextNode = self.tail.prev, self.tail
        prevNode.next = node
        node.prev = prevNode
        nextNode.prev = node
        node.next = nextNode

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
