from tree_class import BinaryTree

def create_tree_one():
    mytree = BinaryTree(17)
    mytree.insertLeft(23)
    mytree.insertRight(5)
    mytree.getRightChild().insertLeft(45)
    mytree.getRightChild().insertRight(23)
    mytree.getRightChild().getLeftChild().insertLeft(2)
    print('\t\t\tTree One\n')
    print('\t\t\t',mytree.getRootVal())
    print('\t\t  ',mytree.getLeftChild().getRootVal(),'\t\t',mytree.getRightChild().getRootVal())
    print('\t\t\t    ',mytree.getRightChild().getLeftChild().getRootVal(),'   ',mytree.getRightChild().getRightChild().getRootVal())
    print('\t\t\t  ',mytree.getRightChild().getLeftChild().getLeftChild().getRootVal())
    return mytree

def create_tree_two():
    mytree = BinaryTree(100)
    mytree.insertLeft(50)
    mytree.insertRight(75)
    mytree.getLeftChild().insertRight(25)
    print('\t\tTree Two\n')
    print('\t    ',mytree.getRootVal())
    print('\t',mytree.getLeftChild().getRootVal(),'\t',mytree.getRightChild().getRootVal())
    print('\t   ',mytree.getLeftChild().getRightChild().getRootVal())
    return mytree

def create_tree_three():
    mytree = BinaryTree(15)
    mytree.insertLeft(20)
    mytree.getLeftChild().insertLeft(25)
    mytree.getLeftChild().getLeftChild().insertLeft(10)
    mytree.getLeftChild().getLeftChild().getLeftChild().insertLeft(5)
    print('\t\t\tTree Three\n')
    print('\t\t\t',mytree.getRootVal())
    print('\t\t      ',mytree.getLeftChild().getRootVal())
    print('\t\t    ',mytree.getLeftChild().getLeftChild().getRootVal())
    print('\t\t  ',mytree.getLeftChild().getLeftChild().getLeftChild().getRootVal())
    print('\t\t',mytree.getLeftChild().getLeftChild().getLeftChild().getLeftChild().getRootVal())
    return mytree

def sum_of_tree(tree):
    sum =0
    if tree!=None:
        sum = sum_of_tree(tree.getLeftChild())
        sum = sum + sum_of_tree(tree.getRightChild())
        sum = sum + (tree.getRootVal())

    return sum

def postorder(tree):
    if tree!= None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print('Adding',tree.getRootVal())

    
print('----------------------------------------------------------')
tree1 = create_tree_one()
postorder(tree1)
print('\nThe Sum of Tree One is:',sum_of_tree(tree1))
print('----------------------------------------------------------')
tree2 = create_tree_two()
postorder(tree2)
print('\nThe Sum of Tree Two is:',sum_of_tree(tree2))
print('----------------------------------------------------------')
tree3 = create_tree_three()
postorder(tree3)
print('\nThe Sum of Tree Three is:',sum_of_tree(tree3))
print('----------------------------------------------------------')

