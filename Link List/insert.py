class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1



    def printList(self):
        current = self.head

        while current is not None:
            print(current.value, end="\t")
            current = current.next

        print()

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp


    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1


linked_list = LinkedList(3)


linked_list.append(12)
linked_list.append(16)
linked_list.append(20)
linked_list.append(25)
linked_list.append(26)

linked_list.printList()

linked_list.insert(1, 5)
linked_list.printList()

linked_list.insert(6, 500)
linked_list.printList()

linked_list.insert(0, 800)
linked_list.printList()

linked_list.insert(12, 600)
linked_list.printList()

