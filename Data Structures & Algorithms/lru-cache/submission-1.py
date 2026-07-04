class ListNode:
    def __init__(self,key=0, val=0, prev=None,next=None):
        self.key=key
        self.val=val
        self.prev=prev
        self.next=next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {} # key: ListNode(key,val)
        self.start = ListNode()
        self.end = ListNode()
        self.start.next = self.end
        self.end.prev = self.start
        

    def get(self, key: int) -> int:
        # if node not in cache, return -1
        if key not in self.nodes:
            return -1
        
        node = self.nodes[key]
        
        # remove node
        node.prev.next, node.next.prev = node.next, node.prev

        # put node at front of list
        self.prependNode(node)
        return node.val



    def put(self, key: int, value: int) -> None:
        # If key already exists
        if key in self.nodes:
            node = self.nodes[key]
            self.removeNode(node)
            self.prependNode(node)
            node.val = value
            return


        # If key doesn't exist
        new_node = ListNode(key=key,val=value)
        self.nodes[key] = new_node

        # put node at front of list
        self.prependNode(new_node)

        self._maybeRemoveLru()

    def removeNode(self, node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev


    def prependNode(self, node) -> None:
        prev_first_node = self.start.next
        self.start.next = node
        node.prev = self.start
        node.next = prev_first_node
        prev_first_node.prev = node

    def _maybeRemoveLru(self) -> None:
        if len(self.nodes) <= self.capacity:
            return
        last_node = self.end.prev
        last_node.prev.next = self.end
        self.end.prev = last_node.prev
        del self.nodes[last_node.key]


        
