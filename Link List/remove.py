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


    def pop_first(self):
        if self.length == 0 or self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            return temp.value

    def pop_last(self):
        # Empty list
        if self.length == 0:
            return None
        else:
            pre = self.head
            temp = self.head

            # Traverse to the last node
            while temp.next:
                pre = temp
                temp = temp.next

            self.tail = pre
            self.tail.next = None
            self.length -= 1

            # If list becomes empty
            if self.length == 0:
                self.head = None
                self.tail = None

            return temp


    def printList(self):
        current = self.head

        while current is not None:
            print(current.value, end="\t")
            current = current.next

        print()


    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop_last()

        prev = self.get(index - 1)
        temp = prev.next

        prev.next = temp.next
        temp.next = None
        self.length -= 1

        return temp



linked_list = LinkedList(3)


linked_list.append(12)
linked_list.append(16)
linked_list.append(20)
linked_list.append(25)
linked_list.append(26)

linked_list.printList()

linked_list.remove(4)

print("After removing:")
linked_list.printList()
