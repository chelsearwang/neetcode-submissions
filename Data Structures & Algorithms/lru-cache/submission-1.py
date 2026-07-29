class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mydict = {}
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.mydict:
            # get cur, pre, nxt
            cur = self.mydict[key]
            pre = cur.prev
            nxt = cur.next
            # remove cur from chain
            pre.next = nxt
            nxt.prev = pre
            # insert cur in front of first
            first = self.head.next
            first.prev = cur
            cur.next = first
            self.head.next = cur
            cur.prev = self.head
            temp = {}
            for k in self.mydict:
                temp[k] = self.mydict[k].value
            print("get " + str(key))
            print(temp)
            return cur.value
        return -1
    # insert at head, remove from tail
    def put(self, key: int, value: int) -> None:
        if key in self.mydict:
            # update value and age and return
            cur = self.mydict[key]
            cur.value = value
            pre = cur.prev
            nxt = cur.next
            # remove cur from chain
            pre.next = nxt
            nxt.prev = pre
            # insert cur in front of first
            first = self.head.next
            first.prev = cur
            cur.next = first
            self.head.next = cur
            cur.prev = self.head
            return
        elif len(self.mydict) == self.cap:
            # remove LRU node from tail
            cur = self.tail.prev
            pre = cur.prev
            pre.next = self.tail
            self.tail.prev = pre
            del self.mydict[cur.key]
            # HOW DO DELETE CUR AAAAH
        # add new node
        first = self.head.next
        new = self.Node(key, value)
        new.prev = self.head
        new.next = first
        self.head.next = new
        first.prev = new
        self.mydict[key] = new
        temp = {}
        for k in self.mydict:
            temp[k] = self.mydict[k].value
        print("put " + str(key) + " " + str(value))
        print(temp)