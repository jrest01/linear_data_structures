from node import Node


node1 = Node
node2 = Node("A", None)
node3 = Node("B", node2)

node1 = Node("C", node3)


# print(node3.data)
# print(node3.next.data)

head = None
for count in range(1,5):
    head = Node(count, head)

while head != None:
    print(head.data)
    head = head.next

print(head)