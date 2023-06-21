

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):

        # if there is not current head, create one
        if not self.head:
            self.head = Node(data)

        # if there is a current head, append to the end of the list
        else:
            # current node is the head
            current = self.head
            # while there is a next node, keep going
            while current.next:
                # set current node to the next node
                current = current.next
            # once there is no next node, set the next node to the new node
            current.next = Node(data)

    # Method to display the Linked List
    def display(self):
        elements = []  # Initialize an empty list
        current_node = self.head  # Start from the head
        while current_node:  # Traverse through the list
            elements.append(current_node.data)  # Add the node data to the list
            current_node = current_node.next  # Move to the next node
        return elements  # Return the list of elements


linkedList = LinkedList()

linkedList.append(1)
linkedList.append(2)
linkedList.append(3)

print(linkedList.display())