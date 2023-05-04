from queues_based_list import ListQueue

food = ListQueue()
food.enqueue('Burger')
food.enqueue('Pasta')
food.enqueue('Piza')

food.traverse()
food.dequeue()
print('*'*10)
food.traverse()
