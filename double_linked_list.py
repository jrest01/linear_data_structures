
class TwoWayNode:
    def __init__(self, data=None, previous=None, next=None):
        self.data = data
        self.next = next
        self.previous = previous
        self.head = None
        self.size = 0 
        
    def add_head(self, data):
        """
            Insert a new Node at the head
        """
        if self.head == None:
            self.head = TwoWayNode(data)
            self.size += 1
        else:
            self.head = TwoWayNode(data, next=self.head)
            self.head.next.previous = self.head
            self.size += 1


    def append(self, data):
        """
            Insert a new Node at the end
        """
        if self.head == None:
            self.add_head(data)
        else:
            node = TwoWayNode(data)
            probe = self.head
            while probe.next:
                probe = probe.next
            probe.next = node
            node.previous = probe
            self.size += 1

    def print(self):
        """
            Print all items of the list 
        """
        probe = self.head
        while probe:
            print(probe.data)
            probe = probe.next
            
    def ordened_print(self):
        """
            Print all the Items with its previos and next item
        """
        probe = self.head
        while probe:
            print('-'*11)
            print(probe.data)
            if probe.previous:
                print(' previous '+probe.previous.data)
            else:
                print(' previous None')
            if probe.next:
                print(' next '+probe.next.data)
            
            else:
                print(' next None')
            probe = probe.next

    def insert(self, data, index):
        """
            Insert an item at the indicated index
        """
        if index > self.size:
            print('El índice supera la cantidad de items')
        else:
            if self.head is None or index <= 0:
                self.add_head(data)
            else:
                
                probe = self.head
                while index > 0 :
                    probe = probe.next
                    index -= 1
                node = TwoWayNode(data,probe.previous,probe)
                probe.previous.next = node
                probe.previous = node
                self.size += 1

    def replace(self, target, new_data):
        """
            Replace a Node with new info
        """
        probe = self.head
        if probe == None:
            print("no items")
        replaced = False
        while probe:
            if probe.data == target:
                probe.data = new_data
                replaced = True
                break
            probe = probe.next
        if replaced:
            print(f'{target} replaced with {new_data}')
        else:
            print(f'{target} not found')

    def delete(self, index):
        """
            Delete a Node with the index
        """
        if index < 0 or index > self.size:
            print("Invalid Index")
        else:
            if index == 0:
                deleted = self.head
                self.head = self.head.next
                print(f'delected: {deleted.data}')
                self.size -= 1
            elif index == self.size-1:
                deleted = self.pop()
            else:
                probe = self.head
                while index > 0:
                    probe = probe.next
                    index -= 1
                deleted = probe
                probe.previous.next = probe.next
                probe.next.previous = probe.previous
                print(f'delected: {deleted.data}')
                self.size -= 1
        
    def pop(self):
        """
            Delete the last Node
        """
        if self.head == None:
            raise Exception("Sorry, no Nodes")
        elif self.size == 1:
            deleted = self.head
            self.head = None
            self.size -= 1
        else:
            probe = self.head
            while probe.next:
                probe = probe.next
            deleted = probe
            probe.previous.next = None
            self.size -= 1
        print(f'delected: {deleted.data}')
        return deleted

    def search(self, data):
        """
            Search an specific node
        """
        if self.head == None:
            raise Exception("Sorry, no Nodes")
        else:
            probe = self.head
            while probe and probe.data != data:
                probe = probe.next
            if probe != None:
                print(f'Found {data} = {probe.data}')
            else:
                print(f'{data} Not Found')

        
    def clear(self):
        """
            Reset the linked list
        """


        