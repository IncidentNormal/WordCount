from collections import Counter
import string
import os.path

class UserVar():
    #Try HOME folder: test.txt.
    home = ''
    try:
        #UNIX:
        home = os.getenv("HOME")
        if home == None:
            #WINDOWS:
            home = os.getenv('USERPROFILE')
        print home
    except:
            home == ''
    filename = 'Darwin C - On The Origin Of Species.txt'
    #Start N as 25
    N = 1000

class WordCount():
    def __init__(self):
        self.checkVariables()
        self.wordCount()
    def checkVariables(self):
        #Check with User via console whether variables are suitable, if not, give them option to change:
        fCheck = True
        nCheck = True
        while fCheck:
            F = raw_input("File to analyse is currently: " + UserVar.filename + " ; is this correct? (Y/N)")
            if F == 'Y' or F == 'y':
                fCheck = False
            elif F == 'N' or F == 'n':
                fNameCheck = True
                while fNameCheck:
                    _filename = raw_input("Please enter full path to file (including filename): ")
                    if os.path.isfile(_filename):
                        UserVar.filename = _filename
                        fCheck = fNameCheck = False
                    else:
                        print 'Invalid path to file, if you are unsure of path or unable to type it into this console easily, this Python script can be manually edited! Variables are in UserVar() class at top (Ctrl + C to exit)'
            else:
                print 'Invalid input, please type either Y or N'
        while nCheck:
            N = raw_input("Script will output the top N most common words, N is currently: " + str(UserVar.N) + " ; is this correct? (Y/N)")
            if N == 'Y' or N == 'y':
                nCheck = False
            elif N == 'N' or N == 'n':
                nNumCheck = True
                while nNumCheck:
                    _N = raw_input("Please enter new value of N: ")
                    if _N.isdigit():
                        UserVar.N = int(_N)
                        nNumCheck = nCheck = False
                    else:
                        print 'Invalid input of N, please input an integer (e.g. 2, 5 or 12)'
            else:
                print 'Invalid input, please type either Y or N'

    def wordCount(self):
        #The actual word count, not as sraightforward as it first seems, need to be quite familiar with string manipulation here:
        with open(UserVar.filename, 'r') as fid:
            fileContents = fid.read()
            #check these are all actually WORDS (i.e. entirely formed of letters, so not getting things like '"We' or 'end.' with punctuation included - set punctuation characters to be removed:
            #use string manipulator 'translate' as this is raw C code, hence fastest.
            fileContents = fileContents.translate(string.maketrans("",""), string.punctuation)
            #upper and lower case characters will be treated differently by any string manipulation function, causing different capitalisations to be classified as different words!
            #set entire text to lowercase, and split by space (' ')
            fileWords = fileContents.lower().split()
            #output length of this list as wordcount, to show its worked:
            print 'Total wordcount:', len(fileWords)

            #use helper function 'Counter.most_common()' to do the word counting, as it is faster than any manual algorithm.
            counter = Counter(fileWords)
            print 'Top', UserVar.N, 'most common words, and the number of times they occur:'
            for word, count in counter.most_common(UserVar.N):
                print word, count
            

WC = WordCount()
