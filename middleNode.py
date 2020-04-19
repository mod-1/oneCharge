import argparse

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def nodePrint(self):
        node = self
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print()


class LinkedList:
    def __init__(self):
        self.head = None

    def listPrint(self):
        node = self.head
        while node is not None:
            print (node.data, end=" ")
            node = node.next
        print()

    # Similiar concept to Floyd cycle detection
    def middleNode(self):
        slow = self.head
        fast = self.head
        while fast is not None:
            fast = fast.next
            if fast is not None:
                slow = slow.next
                fast = fast.next
        slow.nodePrint()


def main(inp):
    # print(inp)
    llist = LinkedList()
    llist.head = Node(inp[0])
    curr = llist.head
    for x in range(1,len(inp)):
        curr.next =  Node(inp[x])
        curr = curr.next
    # llist.listprint()
    llist.middleNode()
    

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", nargs="*", type=int, default=[1,2,3,4,5], help="Enter space separated integers, the fist integer will be the head of the list (default: [1,2,3,4,5])")
    args = ap.parse_args()
    main(args.list)
        