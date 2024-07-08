# assignment: programming assignment 4
# author: Lynelle Goh
# date: 11/17/2022
# file: tree.py is a program that creates and traverses a binary tree; in here, we can evaluate and convert infix, prefix, and postfix
# input: for the binary tree, it can intake a value 
#       for the expression tree, it can intake a postfix expression
# output: for the binary tree, it outputs a binary tree with its roots and their children
#       for the expression tree, it can output an evaluation, inorder, preorder, or postorder of an expression 

from stack import Stack

# most functions were copied and pasted from our assignment where we had to finish our own Binary Tree ADT
class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self,newNode):
      if self.rightChild == None:
        self.rightChild = BinaryTree(newNode)
      else:
        t = BinaryTree(newNode)
        t.rightChild = self.rightChild
        self.rightChild = t
    
    def getRightChild(self):
      return self.rightChild

    def getLeftChild(self):
      return self.leftChild

    def getRootVal(self):
      return self.key

    def setRootVal(self, obj):
        self.key = obj

    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s

class ExpTree(BinaryTree):

    def make_tree(postfix):
        # need the operators for placement of the stuff
        operator = ['+','-','*','/', '^', '(', ')']

        s = Stack()
        
        # go through the list
        for i in postfix:
            tree = ExpTree(i)
            if i in operator:
                # pop out of the stack
                tree.rightChild = s.pop()
                tree.leftChild = s.pop()
            # push into the stack
            s.push(tree)

        return s.pop()
    
    def preorder(tree):
        s = ''
        if tree:
            s += tree.getRootVal()
            # get the children after getting the root
            s += ExpTree.preorder(tree.getLeftChild())
            s += ExpTree.preorder(tree.getRightChild())
        return s

    def inorder(tree):
        s = ''

        if tree:
            # get the children before and after getting the root
            if tree.getLeftChild():
                s += '('
                s += ExpTree.inorder(tree.getLeftChild())
            s += tree.getRootVal()
            if tree.getRightChild():
                s += ExpTree.inorder(tree.getRightChild())
                s += ')'

        return s
      
    def postorder(tree):
        s = ''
        if tree:
            # get the children before getting the root
            if tree.getLeftChild():
                s += ExpTree.postorder(tree.getLeftChild())
            if tree.getRightChild():
                s += ExpTree.postorder(tree.getRightChild())
            s += tree.getRootVal()
        return s

    def evaluate(tree):
        if not tree:
            return 0
        if not tree.getLeftChild() or not tree.getRightChild():
            return tree.getRootVal()

        # recursion
        left = int(ExpTree.evaluate(tree.getLeftChild()))
        right = int(ExpTree.evaluate(tree.getRightChild()))

        # check what operations to perform
        if tree.getRootVal() == '+':
            return left + right
        if tree.getRootVal() == '-':
            return left - right
        if tree.getRootVal() == '*':
            return left * right
        if tree.getRootVal() == '/':
            return left // right
            
    def __str__(self):
        return ExpTree.inorder(self)
   
# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':

    # test a BinaryTree
    
    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild()== None
    assert r.getRightChild()== None
    assert str(r) == 'a()()'
    
    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'
    
    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'
    
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'

    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'

    
    # test an ExpTree
    
    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '(5+(2*3))' 
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0

    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0
    