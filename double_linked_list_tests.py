from double_linked_list import TwoWayNode

lista = TwoWayNode()

lista.add_head('3')
lista.add_head('2')
lista.add_head('1')
lista.append('4')
lista.append('5')
lista.append('6')


lista.insert('0', 0)
# lista.insert('err', 2)
# # lista.print()

# lista.replace('6','7')

# # lista.print()

# lista.ordened_print()

# lista.delete(19)

# lista.print()
# lista.delete(6)
# lista.pop()
lista.print()
lista.search('5')
# lista.ordened_print()