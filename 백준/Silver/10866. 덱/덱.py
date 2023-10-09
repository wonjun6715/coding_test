from collections import deque
import sys
dq = deque()

def push_front(X):
    dq.appendleft(X)
    
def push_back(X):
    dq.append(X)

def pop_front():
    if len(dq) == 0:
        return -1
    return dq.popleft()

def pop_back():
    if len(dq) == 0:
        return -1
    return dq.pop()

def size():
    return len(dq)

def empty():
    if len(dq) > 0:
        return 0
    else:
        return 1

def front():
    if len(dq) > 0:
        return dq[0]
    return -1

def back():
    if len(dq) > 0:
        return dq[-1]
    return -1

N = int(sys.stdin.readline())

for i in range(N):
    answer = sys.stdin.readline().split()
    if answer[0] == 'push_front':
        push_front(int(answer[1]))
    elif answer[0] == 'push_back':
        push_back(int(answer[1]))
    elif answer[0] == 'pop_front':
        print(pop_front())
    elif answer[0] == 'pop_back':
        print(pop_back())
    elif answer[0] == 'size':
        print(size())
    elif answer[0] == 'empty':
        print(empty())
    elif answer[0] == 'front':
        print(front())
    elif answer[0] == 'back':
        print(back())
        