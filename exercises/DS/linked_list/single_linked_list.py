class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, data):
        self.data = data
    def set_next(self, next):
        self.next = next

    def hasNext(self):
        return self.next != None

    class LinkedList(object):
        def __init__(self, node=None):
            self.length = 0
            self.head = node
        def insert_at_begininig(self,data):
            newnode = Node()
            node.data = data
            if self.length == 0:
                self.head = node

            else:
                newnode.next = self.head
                self.head = newnode
            self.length += 1

        def insert_at_end(self,data):
            newnode=Node()
            newnode.data = data
            current = self.head
            if current.next != None:
                current = current.next
            current.next = newnode
            newnode.next = None
            self.length+=1

        def insert_at_position(self,data,pos):
            if pos > self.length or pos < 0:
                return None
            if pos == 0:
                self.insert_at_end(data)
            if pos == self.length:
                self.insert_at_end(data)
            newnode = Node()
            count = 1
            current_node = self.head
            while pos != count:
                current_node = self.next
                count+=1
            newnode.next = current_node.next
            current.next = new_node
            self.length +=1

