class Node:
    def __init__(self, data, parent):
        self._data = data
        self._Child = []
        self._parent = parent

    def addChild(self, data):
        self._Child.append(data)
    
class Tree:
    def Sum(self, node):
        sum = 0
        if len(node._Child) == 0:
            return node._data
        for anak in node._Child:
            sum += self.Sum(anak)
        return sum + node._data

    def sibling(self, node):
        if len(node._parent._Child) == 0:
            return node._data
        elif len(node._parent._Child) == 1:
            return node._data
        else:
            saudara = 0
            for anak in node._parent._Child:
                saudara += anak._data
            return saudara

#TEST CASE
if __name__ == '__main__':
    Root = Node(200, None)
    test1 = Node(23,Root)
    test2 = Node(11,Root)
    test3 = Node(13, test1)
    test4 = Node(57, test1)
    test5 = Node(32, test2)
    test6 = Node(42, test3)
    test7 = Node(51, test3)
    test8 = Node(71,test3)
    test9 = Node(12, test4)
    test10 = Node(15, test4)
    test11 = Node(33, test5)
    test12 = Node(8, test5)
    Root.addChild(test1)
    Root.addChild(test2)
    test1.addChild(test3)
    test1.addChild(test4)
    test2.addChild(test5)
    test3.addChild(test6)
    test3.addChild(test7)
    test3.addChild(test8)
    test4.addChild(test9)
    test4.addChild(test10)
    test5.addChild(test11)
    test5.addChild(test12)
    t = Tree()
    val33 = test11
    val200 = Root
    print(f'Total value of all sibling on node {val33._data} = {t.sibling(val33)}')
    print(f'Total value of node {val200._data} and all of its decendands = {t.Sum(val200)}')