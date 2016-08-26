import sys
import pdb
import os
import traceback,Queue,threading
import subprocess
import re

def sort_nicely(l):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    l.sort( key=alphanum_key )

def main():
    flag = True
    dest_list = []
    pingablelist = []
    nonpingablelist = []

    try:
        ip = sys.argv[1]
    except:
        print "Please run the program as python free_ip_finder.py <XX.XX.XX.> where the parameter can by 10.192.140. for example"
        sys.exit()

    for i in range(1,256):
        dest_list.append(ip+str(i))

    def parallelPing():
        while True:
            destip = q.get()
            try:
                print("\nexecuting ping from my machine to %s\n" %(destip))
                op = subprocess.call(['ping','-c','5',destip])
                if(int(op) == 0 ):
                    pingablelist.append(destip)
                    q.task_done()
                else:
                    nonpingablelist.append(destip)
                    q.task_done()
            except:
                print(traceback.format_exc())
                q.task_done()

    q = Queue.Queue()
    for i in range(len(dest_list)):
        t = threading.Thread(target=parallelPing)
        t.daemon = True
        t.start()

    for dest in dest_list:
        q.put(dest)

    q.join()

    if flag == False:
        return 0

    print "\n\n Please find the list of pingable devices in the : %sX network\n" %(sys.argv[1])
    sort_nicely(pingablelist)
    print pingablelist

    print "\n\n Please find the list of nonpingable devices in the : %sX network\n" %(sys.argv[1])
    sort_nicely(nonpingablelist)
    print nonpingablelist

    return 1

if __name__ == '__main__':
    main()
