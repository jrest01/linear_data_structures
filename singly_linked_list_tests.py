from singly_linked_list import SinglyLinkedList


list = SinglyLinkedList()
for i in range(1,6):
    list.add_head(i)

list.add_head('a')

list.append(0)

list.insert('c',0)

list.replace('c','b')

print('-'*10)
list.print()
print('-'*10)
list.delete(0)
list.print()

list.pop()
print('-'*10)
list.print()

list.search(1)
