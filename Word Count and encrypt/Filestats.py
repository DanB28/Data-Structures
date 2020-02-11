
def filestats(fname):
    ## reads in text file and counts the number
    ## of lines,characters, and words in it 
    lines = 0
    words = 0
    char = 0
    string = open(fname,'r')            ## read the file and puts it into a string

    for line in string:
        wordslist = line.split()        #tokenizes the string to identify the words
                                        #and puts it in a list
        lines+=1                        ## counts the number of lines 
        words += len(wordslist)         ## counts the number of words in the list   
        char += len(line)               ## counts the characters in the line
    print ("The file ",fname," contains: \n",char,"Characters\n"
           ,lines,"line\n",words,"words\n"
           "The top ten most frequent words are:\n ")
    
    wordcount(fname)                    ## the wordcount function

def wordcount(fname):
    ## counts the number of word occurrences in the
    ##file and displays the ten most common
    
    from collections import Counter     ## gets counter method from from collections
 
    words = Counter()                   ## assigns the counter method to a variable 
    string = open(fname,'r').read().lower().replace("'","").replace(",","").replace(".","") ## changes the string to lowercase
                                                                                            ## and removes punctuation to get the words the same 
    words.update(string.split())        ## counts the occurencs of words 
    wordlist = (words.most_common(10))  ## gets the top ten 
    for word in wordlist:               ## iterates through them and prints them out
        print(word,"\n")

    
            
        
        

