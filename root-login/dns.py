import re
import sys
import pdb
import os

def main():

    file_desc = open('/Users/nraamanu/finished-programs/login/setup_info.txt','r')
    contents = file_desc.read()
    setup_dict = eval(contents)

    file_desc.close()

    device_name = sys.argv[1]

    try:
        setup_name,device_name = device_name.split('-')
    except:
        pass

    try:
        ip = setup_dict[setup_name][device_name][0]
    except:
        try:
            ip = re.search('(\d+.\d+.\d+.\d+)',device_name).group(1)
        except:
            try:
                #cmd = "ping -c 1 %s" %(sys.argv[1])
                cmd = "nslookup %s | grep -A 3 'Non-authoritative'" %(sys.argv[1])
                contents = os.popen(cmd).read()
                ip = re.search('(\d+.\d+.\d+.\d+)',contents).group(1)
            except:
                sys.exit(1)

    #print "Device {} ip is : {}" .format(device_name,ip)
    print ip
    return ip

if __name__ == '__main__':
    main()
