stack = []  
not stack  
# True
stack.append(1)  # [1]
stack.append(2)  # [1, 2]
stack.append(3)  # [1, 2, 3]
not stack  
# False
stack
# [1, 2, 3]
stack.pop()  # [1, 2]
# 3
stack.pop()  # [1]
# 2
stack.pop()  # []
# 1
not stack
# True