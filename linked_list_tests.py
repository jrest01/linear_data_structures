from linked_list import SinglyLinkedList


words = SinglyLinkedList()
words.append('egg')
words.append('spam')
words.append('ham')

current = words

# while current:
#     print(words)
#     current = current.next

for word in words.iter():
    print(word)

words.search('spam')
words.search('juice')

words.clear()
for word in words.iter():
    print(word)
