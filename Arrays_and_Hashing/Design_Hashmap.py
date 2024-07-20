class LinkedList:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    def __init__(self):
        self.map = [LinkedList() for i in range(1000)]  # Initialise with 1000 dummy nodes

    def hash(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        cur = self.map[index]
        while cur.next:
            # If key already exists we need to update
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        # If key is not there we add it to the end
        cur.next = LinkedList(key, value)

    def get(self, key: int) -> int:
        index = self.hash(key)
        cur = self.map[index]

        # We can probably start from the dummy node here
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        cur = self.map[index]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)