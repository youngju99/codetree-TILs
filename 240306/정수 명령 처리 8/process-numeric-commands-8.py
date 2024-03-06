class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

class Doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0 # node의 전체 개수 저장

    def push_front(self, data):
        new_node = Node(data)

        if self.node_num == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.node_num += 1

    def push_back(self, data):
        new_node = Node(data)

        if self.node_num == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.node_num += 1

    def pop_front(self):
        res = self.head.data

        if self.node_num == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.node_num -= 1

        return res

    def pop_back(self):
        res = self.tail.data

        if self.node_num == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.node_num -= 1

        return res

    def size(self):
        return self.node_num

    def empty(self):
        if self.node_num == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.node_num == 0:
            return "This list is empty!"
        else:
            return self.head.data

    def back(self):
        if self.node_num == 0:
            return "This list is empty!"
        else:
            return self.tail.data

if __name__ == '__main__':
    N = int(input())
    li = Doubly_linked_list()

    for _ in range(N):
        command = input()

        if command.startswith("push_front"):
            li.push_front(int(command.split()[1]))
        elif command.startswith("push_back"):
            li.push_back(int(command.split()[1]))
        elif command.startswith("pop_front"):
            print(li.pop_front())
        elif command.startswith("pop_back"):
            print(li.pop_back())
        elif command.startswith("size"):
            print(li.size())
        elif command.startswith("empty"):
            print(li.empty())
        elif command.startswith("front"):
            print(li.front())
        elif command.startswith("back"):
            print(li.back())
        else:
            print("Invalid command!")