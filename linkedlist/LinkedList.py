
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("LinkedList is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None


linkedList = LinkedList()
linkedList.insert_at_beginning(5)
linkedList.insert_at_beginning(6)
linkedList.insert_at_beginning(7)
linkedList.insert_at_beginning(8)

linkedList.insert_at_end(4)

linkedList.delete_at_beginning()
linkedList.delete_at_end()

linkedList.traverse()