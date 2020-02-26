class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [None for _ in range(10000)]

    def hashedIndex(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = self.hashedIndex(key)
        if self.map[idx] is None:
            self.map[idx] = Node(key, value)
        else:
            cur = self.map[idx]
            while cur.next is not None:
                if cur.key == key:
                    cur.value = value
                cur = cur.next
            if cur.key == key:
                cur.value = value
            else:
                cur.next = Node(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = self.hashedIndex(key)
        if self.map[idx] is None:
            return -1
        else:
            cur = self.map[idx]
            while cur.next is not None:
                if cur.key == key:
                    return cur.value
                cur = cur.next
            if cur.key == key:
                return cur.value
            else:
                return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = self.hashedIndex(key)
        if self.map[idx] is None:
            return
        else:
            if self.map[idx].key == key:
                self.map[idx] = self.map[idx].next
            else:
                cur = self.map[idx]
                while cur.next is not None:
                    if cur.next.key == key:
                        cur.next = cur.next.next
                        return
                    cur = cur.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)