import queue, sys

n = int(sys.stdin.readline())
queue_list = list()

def enqueue(data):
    queue_list.append(data)
    
def dequeue():
    data = queue_list[0]
    del queue_list[0]
    print(data)


for i in range(n):
    queue_command = sys.stdin.readline().split()
    if queue_command[0] == 'push':
        enqueue(queue_command[1])
        
    elif queue_command[0] == 'pop':
        if len(queue_list) == 0:
            print(-1)
        else:
            dequeue()
            
    elif queue_command[0] == 'size':
        print(len(queue_list))
        
    elif queue_command[0] == 'empty':
        if len(queue_list) == 0:
            print(1)
        else:
            print(0)
            
    elif queue_command[0] == 'front':
        if len(queue_list) == 0:
            print(-1)
        else:
            print(queue_list[0])
            
    elif queue_command[0] == 'back':
        if len(queue_list) == 0:
            print(-1)
        else:
            print(queue_list[-1])

            
    