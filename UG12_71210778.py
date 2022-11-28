class Node:
     
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    
    def __init__(self,parent=None):      
        self._parent = parent

    def addChild(self,parent,data):
        newNode = Node(data)
        parent.children.append(data)
        return newNode
    
    def parent(self):
        return self._parent

    def Sum(self,node):
        sum = 0
        for i in node.children:
            sum += i
        return sum

    def sibling(self,node):
        sum=0
        parent = self.parent()
        for i in parent.children:
            sum += i
        return sum

if __name__ == '__main__':
    val200 = Node(200)
    t = Tree(val200)
    val23 = t.addChild(val200,23)
    val11 = t.addChild(val200,11)
    val13 = t.addChild(val23,13)
    val57 = t.addChild(val23,57)
    val42 = t.addChild(val13,42)
    val51 = t.addChild(val13,51)
    val71 = t.addChild(val13,71)
    val12 = t.addChild(val57,12)
    val15 = t.addChild(val57,15)
    val32 = t.addChild(val11,32)
    val33 = t.addChild(val32,33)
    val8 = t.addChild(val32,8)
    print(f'total value of node {val200.data} and all of its descendants = {t.Sum(val200)}')
    print(f'total value of all sibling on node {val33.data} = {t.sibling(val33)}')