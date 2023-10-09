import sys
queue = []
def push(X):
    queue.append(X)
    
def pop():
    if len(queue) == 0:
        return -1
    num = queue[0]
    queue.remove(num)
    return num

def size():
    return len(queue)

def empty():
    if len(queue) == 0:
        return 1
    else:
        return 0

def front():
    if len(queue) == 0:
        return -1
    return queue[0]

def back():
    if len(queue) == 0:
        return -1
    return queue[-1]
N = int(sys.stdin.readline())

for i in range(N):
    answer = sys.stdin.readline().split()
    if answer[0] == 'push':
        push(answer[1])
    elif answer[0] == 'pop':
        print(pop())
    elif answer[0] == 'size':
        print(size())
    elif answer[0] == 'front':
        print(front())
    elif answer[0] == 'empty':
        print(empty())
    elif answer[0] == 'back':
        print(back())
    
    