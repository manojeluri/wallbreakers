class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.m = [None] * self.size

    def add(self, key: int) -> None:
        index = key % self.size

        if self.m[index] == None:
            self.m[index] = ListNode(key, True)
        else:
            currNode = self.m[index]
            tempHead = currNode
            self.m[index] = ListNode(key, True)
            self.m[index].next = currNode

    def remove(self, key: int) -> None:
        index = key % self.size

        if self.m[index] == None:
            return

        else:
            currNode = self.m[index]
            while currNode:
                if currNode.key == key:
                    currNode.val = False
                    break
                currNode = currNode.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = key % self.size
        if self.m[index] == None:
            return False

        else:
            currNode = self.m[index]
            while currNode:
                if currNode.key == key:
                    if currNode.val == True:
                        return True
                    else:
                        return False
                currNode = currNode.next
            return False