#coding=utf-8
'''
Created on Feb 1, 2016

@author: hualingson@foxmail.com
'''

from src.pipe import simp_job
from src.config import *
from src.singleton import Singleton
from src import platform
from src.ssh import ssh
from src import nl

HELP = '''
help: show this message.
remote: change to remote or back to local.
'''

class Cmd(object):
    __metaclass__ = Singleton
    cmds = {
        'pools':CMD_LIST_POOLS,
        'images':CMD_LIST_IMAGES_IN_POOL,
        'blocks':CMD_GRAB_BLOCK_NAME_PREFIX_SN,
        'objects':CMD_FILTER_OBJECTS,
        'paths':CMD_SHOW_OBJECT_PATH
    }
    cmd = 0
    norm = 1
    
    def __init__(self):
        object.__init__(self)
        self.init()
    
    def init(self):
        self.remote = False
        self.ip = "127.0.0.1"
        self.port = 22
        self.username = "root"
        self.password = "password"
        self.pool = 'rbd'
        self.image = 'test'
        self.sn = '9527'
        self.object = 'huaan'
    
    def __perform(self, cmd_mac):
        cmd, mac = cmd_mac
        cmd = cmd % self.__dict__
        print 'command filled with parameters:', cmd
        if self.remote:
            _ = ssh(self.ip, self.port, self.username, self.password, cmd)
        else:
            _ = simp_job(cmd)
        if _ is not None:
            print 'response:', _
            print mac.findall(_)
    
    def run(self):
        while True:
            _ = raw_input(HELP).lower()
            if 'quit' == _:
                break
            elif 'remote' == _:
                if self.remote:
                    self.init()
                    print 'welcome back'
                else:
                    #todo: check ip
                    self.ip = raw_input(nl('ip'))
                    self.port = raw_input(nl('port'))
                    if self.port.isdigit():
                        self.port = int(self.port)
                    else:
                        self.port = 22
                        print 'port is bad, use default'
                    self.username = raw_input(nl('username'))
                    self.password = raw_input(nl('password'))
                    print 'use remote again back to local'
                self.remote = ~self.remote
            elif 'images' == _:
                self.pool = raw_input(nl('pool'))
            elif 'blocks' == _:
                self.pool = raw_input(nl('pool'))
                self.image = raw_input(nl('image'))
            elif 'objects' == _:
                self.pool = raw_input(nl('pool'))
                self.sn = raw_input(nl('sn'))
            elif 'paths' == _:
                self.pool = raw_input(nl('pool'))
                self.object = raw_input(nl('object'))
            if Cmd.cmds.has_key(_):
                self.__perform(Cmd.cmds.get(_))
            else:
                print 'commands supported below:'
                print Cmd.cmds.keys()

if __name__ == '__main__':
    Cmd().run()
