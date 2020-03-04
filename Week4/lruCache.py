class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = ListNode("head", "head")
        self.tail = ListNode("tail", "tail")
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {}

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        else:
            cur_node = self.hashmap[key]
            cur_node.prev.next = cur_node.next
            cur_node.next.prev = cur_node.prev

            next = self.head.next
            cur_node.prev = self.head
            self.head.next = cur_node
            cur_node.next = next
            next.prev = cur_node
            return cur_node.value

    def put(self, key: int, value: int) -> None:
        if self.size >= self.capacity:
            # if key in hashmap:
            # make this key the most recent key
            if key in self.hashmap:
                cur_node = self.hashmap[key]
                cur_node.value = value
                cur_node.prev.next = cur_node.next
                cur_node.next.prev = cur_node.prev
                next = self.head.next
                self.head.next = cur_node
                cur_node.prev = self.head
                cur_node.next = next
                next.prev = cur_node
            else:
                # remove the least recent and insert the new key
                old_node = self.tail.prev
                old_node.prev.next = self.tail
                self.tail.prev = old_node.prev
                self.hashmap.pop(old_node.key)
                cur_node = ListNode(key, value)
                self.hashmap[key] = cur_node
                next = self.head.next
                self.head.next = cur_node
                cur_node.prev = self.head
                cur_node.next = next
                next.prev = cur_node
                self.size += 1
        else:
            if key in self.hashmap:
                cur_node = self.hashmap[key]
                cur_node.value = value
                cur_node.prev.next = cur_node.next
                cur_node.next.prev = cur_node.prev

                next = self.head.next
                self.head.next = cur_node
                cur_node.prev = self.head
                cur_node.next = next
                next.prev = cur_node
            else:
                cur_node = ListNode(key, value)
                self.hashmap[key] = cur_node
                next = self.head.next
                self.head.next = cur_node
                cur_node.prev = self.head
                cur_node.next = next
                next.prev = cur_node
                self.size += 1

            # update its value and make it the  most recent
            # else:
            # insert a new key at the beginning

    def isEmpty(self):
        return self.getSize() == 0

    def getSize(self):
        return self.size

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)