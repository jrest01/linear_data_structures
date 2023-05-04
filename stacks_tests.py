from stacks import Stack

food = Stack()
food.push('burger')
food.push('pasta')
food.push('pizza')
# print('se elima: '+food.pop())
print('top: '+food.peek())


for foodies in food.iter():
    print(foodies)

print('-'*10)
food.search('burgesr')