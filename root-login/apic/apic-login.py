import sys,pdb,os
import paramiko
import BeautifulSoup
import subprocess
import time

def generate_token(ip):

    try:
        username = 'rescue-user'
        password = 'ins3965!'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username,password=password,key_filename='/dev/null',timeout=10)

    except:
        username = 'admin'
        password = 'ins3965!'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username,password=password,key_filename='/dev/null',timeout=10)

    si,so,se = ssh.exec_command('acidiag dbgtoken')
    token = so.readlines()[0].strip()
    return token

def generate_root_passwd(token):

    #sys.stdout = open(os.devnull, "w")
    #sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    contents = os.popen('curl http://git.insieme.local/cgi-bin/generateRootPassword.py?key=%s' %(token)).read()
    #sys.stdout = sys.__stdout__
    soup = BeautifulSoup.BeautifulSoup(contents)
    root_passwd = str(soup.find('code').text)
    return root_passwd

def main(ip):

    token = generate_token(ip)
    root_passwd = generate_root_passwd(token)

    print root_passwd
    return root_passwd

if __name__ == '__main__':
    main(sys.argv[1])
