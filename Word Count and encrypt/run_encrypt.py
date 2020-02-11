def digitencode():
    ##reads in a file and puts its contents into a library
    digitcode = {}
    file = open("digitencode.txt",'r')
    for line in file:
        (k,val) = line.split()
        digitcode[(k)]=val
    return digitcode

def find_key(digits, value):
        ## takes the value of the phrase and finds it in the dictionary and returns it's key
        return [k for k, val in digits.items() if val == value][0]

def encode(p,k):
    ## encodes a given phrase based on a key that is entered as well
    lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
             ,'n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
             'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
    
    digits = digitencode()## gets the file for the library and assigns it to a variable
    phrase = p
    index_key = k
    key = int(index_key)
    i=0
    newphrase = ""
    while i< len(phrase):
        if phrase[i].isdigit(): ##checks to see if character is digit 
            index = phrase[i]
            enindex = digits[index]
            newphrase = newphrase+enindex
    
        elif phrase[i].islower():## checks to see if character is lowercase
            index = lower.index(phrase[i])
            valueindex = index+key
            if valueindex < len(lower):
                enindex = lower[index+key]
                newphrase = newphrase+enindex
                
            elif valueindex > len(lower):
                newindex = (valueindex-len(lower))
                enindex = upper[newindex]   
                newphrase = newphrase+enindex
                   
        elif phrase[i].isupper() or ' ':# checks to see if character is upp case 
            index = upper.index(phrase[i])
            valueindex = index+key
            if valueindex < len(upper):
                enindex = upper[index+key]
                newphrase = newphrase+enindex

            elif valueindex >len(upper):
                newindex = (valueindex-len(upper))
                enindex = lower[newindex]   
                newphrase = newphrase+enindex    
        i+=1
    return newphrase
    print(newphrase)



def decode(p,k):
    ## decodes the encoded phrase back to the orginal phrase based on the same key
    ## in stead of adding the key to the index it subtracts it and goes backwards of encoding 
    lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
             'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
    digits = digitencode()
    
    phrase = p
    index_key = k
    key = int(index_key)
    i=0
    newphrase = ""
         

    while i< len(phrase): ## iterates through the phrase
        
        if phrase[i].isdigit(): ##checks to see if the character is a digit
            index = phrase[i]
            enindex = digits[index]
            newphrase = newphrase+enindex

        elif phrase[i] in digits.values():
            index = phrase[i]
            enindex = find_key(digitencode(),index)
            newphrase = newphrase+enindex
            
            
        elif phrase[i].islower():## checks if character is lowercase
            index = lower.index(phrase[i])
            valueindex = index-key
            if valueindex < 0:
                enindex = upper[index-key]
                newphrase = newphrase+enindex
            else:
                enindex = lower[index-key]
                newphrase = newphrase+enindex
                
        elif phrase[i].isupper() or ' ':## checks to see if character is uppercase
            index = upper.index(phrase[i])
            valueindex = index-key
            if valueindex < 0:
                enindex = lower[index-key]
                newphrase = newphrase+enindex
            else:
                enindex = upper[index-key]
                newphrase = newphrase+enindex

                
        elif valueindex >len(upper):
            newindex = (len(lower))
            enindex = lower[newindex]   
            newphrase = newphrase+enindex

        i+=1
    return newphrase    
    print(newphrase) 
   

def run_encrypt():
    ## Runs the program as a whole when entered into idle
    phrase = input("Please enter a phrase: ")
    key_value = int(input("Please enter a key Value between 1 and 9: "))
    choice = input("Enter 1 to encode or enter 2 to decode: ")
    if key_value<=9 and key_value>=1:
        if choice == '1':
            print(encode(phrase,key_value))
            
        elif choice == '2':
            print(decode(phrase,key_value))
            
        else:
            print("You did not enter a correct choice, Enter 1 to encode or enter 2 to decode")
    else:
        print("Key value is not in the range of 1 to 9")
    

run_encrypt()
## will run the program strait from here if not entered in idle 
