import sys,pdb,os,re
import paramiko
import telnetlib
import BeautifulSoup
import subprocess
import time

from sh import python

def populate_tor_info(ip):
    fd = open('switch.txt','r')
    contents = fd.read().strip()
    tor_dict = eval(contents)
    fd.close()
    return tor_dict[ip]

def generate_token(ip):

    try:
        username = 'admin'
        password = 'ins3965!'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username,password=password,key_filename='/dev/null',timeout=10)
        si,so,se = ssh.exec_command('acidiag dbgtoken')
        token = so.readlines()[0].strip()
        root_passwd = generate_root_passwd(token)

    except:
        switch_name = populate_tor_info(ip)

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('10.193.180.62', username='nraamanu',password='',key_filename='/dev/null',timeout=10)
        si,so,se=ssh.exec_command('cd /auto/AVS1/UPGRADE_SETUP/;python getnodedbgtoken.py admin ins3965! %s' %(switch_name))

        contents = so.read()
        root_passwd = re.search('quit\n(.*)\n',contents).group(1)
   
    ssh.close()
    return root_passwd

def generate_root_passwd(token):

    contents = os.popen('curl http://git.insieme.local/cgi-bin/generateRootPassword.py?key=%s' %(token)).read()
    soup = BeautifulSoup.BeautifulSoup(contents)
    root_passwd = str(soup.find('code').text)
    return root_passwd

def main(ip):
    root_passwd = generate_token(ip)
    #fd = open('root.txt','w')
    #fd.write(root_passwd) 
    #fd.close()
    print root_passwd

if __name__ == '__main__':
    main(sys.argv[1])
