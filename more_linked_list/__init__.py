class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while (start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        aux = head
        acum = []
        head_acum = []
        while aux:
            if aux.data not in acum:
                acum.append(aux.data)
                head_acum.append(aux)
            aux = aux.next
        if len(head_acum) == 1:
            head_acum[0].next = None
        for idx in range(len(head_acum) - 1):
            if len(head_acum) - 2 == idx:
                head_acum[idx + 1].next = None
            head_acum[idx].next = head_acum[idx + 1]
        return head_acum[0]


mylist = Solution()
T = 6
t_data = [3,
9,
9,
11,
11,
11,
11,
89,
89,
100,
100,
101,
102,
103,
108,
200,
250,
250,
250,
250]
head = None
for i in t_data:
    data = i
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)
