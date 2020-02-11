##############################################################################################
'''
Dan Bailey
Project Three
11/23/16    
    This program's objective is to read in a file that has a list of characters that have a code
associated with them, and based on if the code reads a one or zero, the program will create a tree
and add left and right nodes accordingly, and place the character at the last node based on the
code that reads in.
    when all of the characters are placed into the tree, the program will then
read in a code made of the character codes and decode
it into the orginal message. If there are any errors in the code or the decoding scheme, it will then
throw a message stating so and end the program. This program does not read in numbers of symbols,
just alphabetical characters. I have 6 additional test cases in the Bailey_proj3_test folder, other than
the 3 given for us to use.

There is also a TEST summary file  of all the test cases and expected out puts and why i
used them as test cases.

NOTE: if ran from commmand line each time a new file is to be read in with the function Bailey_proj3('file')
the system had to be reset. so for instance, exit out of cammand line and run again with new file.


'''
##############################################################################################
from tree_class import BinaryTree
import sys

codelist = []
code = []
decodelist = []
message = []
numCount = 0

def Main(file):                 # takes in all the other function to be ran and calculates the bits, characters, and compression ratio
    decode(file)                        # after the  program creates the tree and decodes the message. 
    print('Success:',message)
    numCount = len(message)
    print('Number of bits:',len(code))
    print('Number of characters:',numCount)
    print('Compression Ratio:',((len(code))/(8*numCount)*100),'%')
    print('-------------------------------------------------------------------------------')
    sys.exit()


                                            #getcode function gets the just "decode" the code to decode
def getcode(file):
    codefile = open(file,'r')
    for line in codefile:
        if line == line.strip('\n'):
            for i in line:
                code.append(i)
    return code


                                            #readfile function reads in a file and puts the contents into a list(also gets just
                                            #the decode list from the getcode function)
def readFile(file):
    codefile = open(file,'r')
    for line in codefile:
        line = line.strip()
        temp = []
        if line =='':
            getcode(file)                   #if line is empty calls the getcode function to get just the code to decode and returns the the code list
            return codelist
        for i in line:
            char = i
            temp.append(char)
        codelist.append(temp)
     
def createtree(codelist):                   #createtree function creates a tree based on the code given in the code list and sets                                          # the code represents
    mytree = BinaryTree('')                 # the character to a lead at the end of the path
    temp = mytree
    
    for line in codelist:
        for char in line[1:]:
            if char == '0':                     # if the code is a "0" it gets the left child and checks if it is equal to none and if it is
                if temp.getLeftChild() == None: # it inserts a new node to the left
                    temp.insertLeft('')
                temp = temp.getLeftChild()
                
            if char == '1': 
                if temp.getRightChild() == None: # if the code is a "1" is gets the right child and sets a new node right if it equals none 
                    temp.insertRight('')
                temp = temp.getRightChild()
                
            if temp.getRootVal().isalpha(): # error check for invalid code, if one of the children is not empty or has something in it, throws an error message
                print('ERROR: The code in the file is not valid.')
                sys.exit()
                
        temp.setRootVal(line[0])            # assigns the leaf to what is in the first index of the code list 
        temp = mytree          
    return mytree                           # returns tree when there areno more lines in the code list 

def postorder(tree):                        # if you want to travers through the tree and see whats in it you can call the postorder function
    if tree!=None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def decode(file):                           # takes the decode list and traverses through the tree based on whether the code is a one or zer0,
    readFile(file)                          # if it comes to the end of the path or if the leaf equal a character, it appends it to a list to be
    mytree = createtree(codelist)           # the message that is decoded.
    temp = mytree
    
    for num in code:
        
        if num =='0':
            temp = temp.getLeftChild()
            if temp == None:
                print('Error: Cannot Decode Message')           # if the end of the list or the leaf has nothing in it it will throw an error message 
                sys.exit()                                      # stating that the decode code is not valid, also if it has a number or symbol
            temp2 = temp.getRootVal()                           # it will state can not decode message as well as this program does not take in 
            if temp2.isalpha():                                 # those characters to be in the code. 
                message.append(temp2)
                temp = mytree
                
        if num == '1':
            temp = temp.getRightChild()
            if temp == None:
                print('Error: Cannot Decode Message')
                sys.exit()
            temp2 = temp.getRootVal()
            if temp2.isalpha():
                message.append(temp2)
                temp = mytree

    return message                      # once the function has reached the end of the decode code, it will return the decoded message.  

#Main('invalid_one.txt')            # runs the program
#Main('invalid_two.txt')            # runs the program
#Main('valid_one.txt')            # runs the program
Main('valid_two.txt')            # runs the program











