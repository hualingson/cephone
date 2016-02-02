'''
Created on Feb 2, 2016

@author: bob@huashanpai.net
'''
import paramiko
from src import platform
from src import tb

CMD_SSH = 'ssh %(user)s@%(ip)s "%(command)s"' #alternative

def ssh(ip,port,username,password,command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,port,username,password,timeout=9)
        __stdin, stdout, __stderr = ssh.exec_command(command)
        out = stdout.readlines()
        return platform.linesep.join(out)
        print '%s\tOK\n'%(ip)
        ssh.close()
    except:
        print '%s\tError\n'%(ip)
        tb.print_exc()

if __name__ == '__main__':
    ssh('10.10.3.153',22,'root','123qwe','date')
