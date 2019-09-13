import sys,re

def main():

    file_desc = open('/Users/nraamanu/finished-programs/login/setup_info.txt','r')
    contents = file_desc.read()
    setup_dict = eval(contents)

    file_desc.close()

    switch_info = {}

    for setup in setup_dict.keys():

        for device in setup_dict[setup].keys():

            try:
                if re.search('leaf',device):
                    switch_info[setup_dict[setup][device][0]] = setup+'-'+device
                elif re.search('spine',device):
                    switch_info[setup_dict[setup][device][0]] = setup+'-'+device
            except:
                continue

    file_desc = open('switch.txt','w')
    to_be_written = str(switch_info)
    file_desc.write(to_be_written)
    file_desc.close()

if __name__ == '__main__':
    main()
