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
        return True

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
        print(temp.value)
        return True


linked_list = LinkedList(3)


linked_list.append(12)
linked_list.append(16)
linked_list.append(20)
linked_list.append(25)
linked_list.append(26)


linked_list.printList()

linked_list.get(1)

