import sys

def get_current_status():

    current_contents={}
    f = open('status.txt','r')
    contents = f.read().strip()
    f.close()
    content_array = contents.split("\n")
    for line in content_array:
        setup_name,setup_status,username,comments = line.split(',')
        current_contents[setup_name] = [setup_status,username,comments]

    return current_contents

def main():

    try:
        setup_name = sys.argv[1]
        status_dict = get_current_status()
    except:
        print "\nHit exception. Setup name maybe incorrect or setup entry may not be present in the setup list. Please check. \n"
    finally:
        if status_dict[setup_name][0] == 'Locked':
            sys.exit(1)
        else:
            sys.exit(0)

if __name__ == '__main__':
    main()
