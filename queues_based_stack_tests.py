from queues_based_stack import Queue

number = Queue()
number.enqueue(5)
number.enqueue(6)
number.enqueue(7)
number.enqueue(8)

print(number.inboud_stack)
print(number.dequeue())
print(number.outboud_stack)
