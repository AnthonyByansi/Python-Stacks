# A stack in data structutres and algorithms---- is a squence of pilled elements#

#create a stack 
def create_stack():
    stack = []
    return stack 

# create an empty stack
def check_empty(stack):
    return len(stack) == 0

# Add items to your stack 
def push (stack, item ):
    stack.append(item)
    print("Added item: " + item )
    
# Then pop an item. from the stack 
def pop(stack):
    if check_empty(stack):
        return "Our stack is empty"
    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))

print("Removed an item: " + pop(stack))
print("stack after removing/popping an an item: " + str(stack))

    # comments are much much welcome and appreciated 🥰. 
    