import sys,os,re,time
import pdb
from subprocess import Popen
import getopt

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)', text) ]

def get_current_status():

    current_contents={}
    f = open('status.txt','rw')
    contents = f.read().strip()
    f.close() 
    content_array = contents.split("\n")
    for line in content_array:
        setup_name,setup_status,username,comments = line.split(',')
        current_contents[setup_name] = [setup_status,username,comments]
       
    return current_contents

def lock_setup(setup_name,comments,username,current_contents):
    setup_dict = get_setup_dict()
    setups = get_same_setups(setup_name,setup_dict)
    for setup in setups:
        current_contents[setup] = ['Locked',username,comments]
    f = open('status.txt','w')
    keys = current_contents.keys()
    keys.sort(key=natural_keys)
    for entry in keys:
        f.write("%s,%s,%s,%s\n" %(entry,current_contents[entry][0],current_contents[entry][1],current_contents[entry][2]))
    f.close()

def unlock_setup(setup_name,username,current_contents):
    if current_contents[setup_name][1] == username:
        setup_dict = get_setup_dict()
        setups = get_same_setups(setup_name,setup_dict)
        for setup in setups:
            current_contents[setup] = ['Unlocked','','']
        f = open('status.txt','w')
        keys = current_contents.keys()
        keys.sort(key=natural_keys)
        for entry in keys:
            f.write("%s,%s,%s,%s\n" %(entry,current_contents[entry][0],current_contents[entry][1],current_contents[entry][2]))
        f.close()
    elif current_contents[setup_name][0] == 'Unlocked':
        print "\n ****** Setup %s is already Unlocked ****** \n" %(setup_name)
        
    else:
        global_flag = 1
        print "\n ******You should be logged in as %s to unlock this setup! ****** \n"%(current_contents[setup_name][1])

def display_setup_status():     
    f = open('status.txt','rw')
    contents = f.read().strip()
    f.close() 
    content_array = contents.split("\n")
    print "Setup status summary:"
    print "======================\n"
    print "Setup name \t\t  Status \t\t Username \t\t Comments \n"
    print "============================================================================================================\n"
    for line in content_array:
        setup_name,setup_status,username,comments = line.split(',')
        print " %s \t\t  %s \t\t %s \t\t %s\n" %(setup_name,setup_status,username,comments)
    
def get_username():
    cmd = "whoami"
    username = os.popen(cmd).read().strip()
    return username

def get_same_setups(setup,setup_dict):
 
    same_setup = setup_dict[setup].split(',')
    return same_setup
    
def get_setup_dict():

    setup_dict = {}
    f=open('same_setups.txt','r')
    contents = f.read().strip()
    f.close()
    for line in contents.split('\n'):
        key,values = line.split(':')
        setup_dict[key] = values

    return setup_dict

def main(argv):

    global_flag = 0
    current_contents = get_current_status()
    os.system('clear')

    try:
        opts, args = getopt.getopt(argv,"l:u:s:c")
        if opts[0][0] == '-l':
            setup_name = opts[0][1]
            comment = argv[3]
            username = get_username()
            if (current_contents[setup_name][1] != username) and (current_contents[setup_name][0] == 'Unlocked'):
                print "Locking setup %s with comments - %s. User locking is - %s" %(setup_name,comment,username)
                lock_setup(setup_name, comment, username, current_contents)
            elif (current_contents[setup_name][1] == '') and (current_contents[setup_name][0] == 'Unlocked'):
                print "Locking setup %s with comments - %s. User locking is - %s" %(setup_name,comment,username)
                lock_setup(setup_name, comment, username, current_contents)
            elif (current_contents[setup_name][1] == username):
                print "Locking setup %s with comments - %s. User locking is - %s" %(setup_name,comment,username)
                lock_setup(setup_name, comment, username, current_contents)
            else:
                global_flag = 1
                print "\n\n ****** Setup %s is currently locked by user %s, With comments - %s ****** \n\n" %(setup_name,current_contents[setup_name][1],current_contents[setup_name][2])
        elif opts[0][0] == '-u':
            setup_name = opts[0][1]
            if current_contents[setup_name][1] == 'Unlocked':
                print "\n Setup is already unlocked!!\n"
            else:
                username = get_username()
                unlock_setup(setup_name,username,current_contents)
        elif opts[0][0] == '-s':
            setup_name = opts[0][1]
            current_contents = get_current_status()
            if current_contents[setup_name][0] == 'Locked':
                global_flag = 1

        time.sleep(1)
        display_setup_status() 
        if global_flag == 1:
            return 0
        else:
            return 1

    except:
        print "Following are the usages possible: \n"
        print "For Locking :: python lock_setup.py -l orion4 -c \"Using for manual testing\"" 
        print "For Unlocking :: python lock_setup.py -u orion4" 
        print "For Displaying :: python lock_setup.py -s orion4\n" 
        sys.exit()
 
if __name__ == '__main__':
    main(sys.argv[1:])
