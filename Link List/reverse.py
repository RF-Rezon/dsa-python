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

    def printList(self):
        current = self.head

        while current is not None:
            print(current.value, end="\t")
            current = current.next

        print()

    # def reverse(self):
    #     temp = self.head
    #     self.head = self.tail
    #     self.tail = temp
    #
    #     after = temp.next
    #     before = None
    #
    #     for _ in range(self.length):
    #         after = temp.next
    #         temp.next = before
    #         before = temp
    #         temp = after



    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp











linked_list = LinkedList(3)


linked_list.append(12)
linked_list.append(16)
linked_list.append(20)
linked_list.append(25)
linked_list.append(26)

linked_list.printList()
print('Here head is:', linked_list.head.value)
print('Here Tail is:', linked_list.tail.value)

linked_list.reverse()
print('After reverse.....')
linked_list.printList()
print('Here head is:', linked_list.head.value)
print('Here Tail is:', linked_list.tail.value)

