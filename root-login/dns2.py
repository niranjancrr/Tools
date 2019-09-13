import re
import sys
import os
import pdb

def main():

    cmd = "nslookup %s | grep -A 3 'Non-authoritative'" %(sys.argv[1])
    contents = os.popen(cmd).read()

    try:
        ip = re.search('(\d+.\d+.\d+.\d+)',contents).group(1)
        print ip
        return ip
    except:
        print "Incorrect DNS information. Please check if your DNS name is correct."

if __name__ == '__main__':
    main()
