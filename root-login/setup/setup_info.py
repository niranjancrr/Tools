import sys,re

def sort_nicely( l ):
    """ Sort the given list in the way that humans expect.
    """
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    l.sort( key=alphanum_key )

def main():

    try:
        setup_name = sys.argv[1]

        file_desc = open('/Users/nraamanu/finished-programs/login/setup_info.txt','r')
        contents = file_desc.read()
        file_desc.close()

        all_setup_info = eval(contents)
        setup_info = all_setup_info[setup_name]

        print "\n{} Setup info:\n" .format(setup_name)
        counter = 0
        temp_info = setup_info.keys() 
        sort_nicely(temp_info)
        for device_name in temp_info:
            counter+=1
            print "{:3}{:5} {:10} {:20} {:10} {:20}" .format(counter,'.',device_name,setup_info[device_name][0],setup_info[device_name][1],setup_info[device_name][2])
            #print "%-3d. %-10s %15s %20s %20s" %(counter,device_name,setup_info[device_name][0],setup_info[device_name][1],setup_info[device_name][2])

    except:
        try:
            print "Setup {} may not be included in the setup database. Please check!" .format(setup_name)
        except:
            print "Usage : info <setup-name>"
    

if __name__ == '__main__':
    main()
