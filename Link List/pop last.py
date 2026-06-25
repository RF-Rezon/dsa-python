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

    # --------------------------------------------------------#

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


linked_list = LinkedList(3)

linked_list.append(12)
linked_list.append(16)
linked_list.append(20)
linked_list.append(25)
linked_list.append(26)


linked_list.printList()

print('Head:', linked_list.head.value)
print('Tail:', linked_list.tail.value)
print('Length:', linked_list.length)


linked_list.pop_last()
print('After pop last:')
linked_list.printList()


print('Head:', linked_list.head.value)
print('Tail:', linked_list.tail.value)
print('Length:', linked_list.length)