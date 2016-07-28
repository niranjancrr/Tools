import sys
import pdb
import re

def main():
    print "you have chosen to open the file : %s" %sys.argv[1]
    pdb.set_trace()
    try:
        dictionary = {}
        f = open(sys.argv[1],'r')
        list = f.read().split(' ')
        for word in list:
            word = word.strip('\'"|\n.<>?/\{}[]:,-_!@#$%^&*()').lower()
            try:
                dictionary[word] = dictionary[word] + 1
            except:
                dictionary[word] = 1

        for word in dictionary.keys():
            print " \"%s\" is repeated %d times" %(word,dictionary[word]) + "\n" 
    except:
        print "the file %s does not exist in the given directory" 

if __name__ == '__main__':
    main()
