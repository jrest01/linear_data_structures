from node import Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0 

    def add_head(self, data):
        """
            Insert a new Node at the head
        """
        self.head = Node(data,self.head)
        self.size += 1

    def append(self, data):
        """
            Insert a new Node at the end
        """
        if self.head == None:
            self.add_head(data)
        else:
            node = Node(data, None)
            probe = self.head
            while probe.next :
                probe = probe.next
            probe.next = node
            self.size += 1

    def insert(self, data, index):
        """
            Insert a new Node at the index
        """
        if index > self.size:
            print("El indice supera la cantidad de nodos")
        else:
            if self.head is None or index <= 0:
                node = Node(data, self.head)
                self.head = node
            else:
                probe = self.head
                while probe.next != None and index > 1:
                    probe = probe.next
                    index -= 1
                node = Node(data, probe.next)
                probe.next = node
                self.size += 1

    def replace(self, target, new_data):
        """
            Replace a Node with new info
        """
        probe = self.head
        if probe == None:
            print("no items")
        else:
            while probe.data != target and probe.next != None:
                probe = probe.next
            if probe.data == target:
                probe.data = new_data
                print(f"{target} replaced with {new_data}")
            else:
                print(f"{target} not found")

    def delete(self, index):
        """
            Delete a Node with the index
        """
        probe = self.head
        if probe == None:
            print("no items")
        elif index == 0:
            removed = probe.data
            self.head = probe.next
            print(f"Node: {removed} deleted.")
        else:
            if index == 1:
                pass
            else:
                while probe.next != None and index > 1:
                    probe = probe.next
                    index -= 1
            removed = probe.next.data
            probe.next = probe.next.next
            print(f"Node: {removed} deleted.")
            self.size -= 1

    def pop(self):
        """
            Delete the last Node
        """
        probe = self.head
        if probe == None:
            print("no items")
        else:
            while probe.next.next:
                probe = probe.next
            removed = probe.next
            probe.next = None
            self.size -= 1
            print(f"Ultimo nodo {removed.data} eliminado.")

    def search(self, data):
        """
            Search an specific node
        """
        probe = self.head
        if probe == None:
            print("no items")
        while probe and probe.data != data:
            probe = probe.next
        if probe:
            print(f'{data} found')
        else:
            print(f'{data} NOT found')

    def print(self):
        probe = self.head
        while probe:
            print(probe.data)
            probe = probe.next
        
    def clear(self):
        self.head = None
        self.size = 0