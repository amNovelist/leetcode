class LinkNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = LinkNode(value, None)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
        self.length+=1

    def prepend(self, value):
        old_head = self.head
        new_node = LinkNode(value, old_head)

        if old_head:
            new_node.next = old_head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

        self.length+=1

    def insert(self, value, index):
        if index == 0:
            self.prepend(value)

        elif index == self.length:
            self.append(index)

        else:
            curr_node = self.head
            for i in range(index-1):
                curr_node = curr_node.next
            next_for_new_node = curr_node.next

            new_node = LinkNode(value, next_for_new_node)
            curr_node.next = new_node
        self.length += 1

    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            self.length -=1
        else:
            curr_node = self.head
            for i in range(index - 1):
                curr_node = curr_node.next
            new_next_node = curr_node.next.next
            curr_node.next = new_next_node
            self.length -=1

    def traverse(self):
        curr_node = self.head
        while curr_node:
            print(f"{curr_node.value} -> ", end="")
            curr_node = curr_node.next
        print("\n")

linked_list = LinkedList()
linked_list.traverse()
linked_list.insert(5, 0)
linked_list.traverse()
linked_list.append(4)
linked_list.traverse()
linked_list.prepend(2)
linked_list.traverse()
linked_list.insert(19, 1)
linked_list.traverse()
linked_list.insert(18, 4)
linked_list.traverse()
linked_list.delete(2)
linked_list.traverse()
linked_list.delete(2)
linked_list.traverse()