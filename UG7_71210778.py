class PrefixConverter:
    def __init__(self):
        self.stackList = ['?']
# method untuk menambahkan data baru
    def push(self,data):
        self.stackList.append(data)
# method untuk melihat data paling atas
    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "Isi Stack Kosong"
# method untuk menghapus data palin atas
    def pop(self):
        if self.stackList:
            data = self.stackList.pop(-1)
            return data
        else:
            return "Isi Stack Kosong"
    def cekValidExpression(self,expression):
        if expression == "+" or expression == "-":
            return 1
        elif expression == "*" or expression == "/":
            return 2
        elif expression in "^":
            return 3
        return 0

    def infixToPrefix(self,expression):
        prefix=""
        for i in expression:
            if(len(expression)%2==0):
                print("Incorrect infix expr")
                return False
            elif(self.infixToPrefix(i)):
                prefix +=i
            elif(i in '+-*/^'):
                while (len(self.stackList)and [self.peek()]):
                    prefix+=self.pop()
                self.push(i)
            elif i is '(':
                self.push(i)
            elif i is ')':
                o=self.pop()
                while o!='(':
                    prefix +=o
                    o=self.pop()
            print(prefix)
                #end of for
        while len(self.stackList):
            if(self.peek()=='('):
                self.pop()
            else:
                prefix+=self.pop()
                print(prefix)
        return prefix


# Test Case
if __name__ == '__main__':
    expresi1 = PrefixConverter()
    print(expresi1.infixToPrefix("1+2+3*4/2-1"))
    print(expresi1.infixToPrefix("A * (B + C) / D"))
    print(expresi1.infixToPrefix("(1+2)*3"))
    print(expresi1.infixToPrefix("20 * 3 - 10 + 289"))
    print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))