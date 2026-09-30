class Node:
    def __init__(self,key=0,val=0,prev=None,next=None):
        self.key=key
        self.val=val
        self.prev=prev
        self.next=next

class LRUCache:

    def __init__(self, capacity: int):
        self.first = Node()
        self.last = Node()
        self.first.next=self.last
        self.last.prev=self.first
        self.capacity=capacity
        self.nodes = {}


    def get(self, key: int) -> int:
        if key not in self.nodes: return -1
        node = self.nodes[key]

        self.removeNode(node)
        self.insertNode(node)

        return node.val

        

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.removeNode(self.nodes[key])
        new_node = Node(key,value)
        self.nodes[key] = new_node
        node = self.nodes[key]
        self.insertNode(node)
        self.maybeEvict()
        
    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def insertNode(self,node):
        node.next = self.first.next
        self.first.next.prev = node
        node.prev = self.first
        self.first.next=node

    def maybeEvict(self):
        if len(self.nodes) <= self.capacity:
            return
        del self.nodes[self.last.prev.key]
        self.removeNode(self.last.prev)
