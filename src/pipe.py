#coding=utf-8
'''
Created on Feb 1, 2016

@author: hualingson@foxmail.com
'''

from src import mthread
from src import subprocess
from src import tb

def simp_job(cmd):
    try:
        sp = subprocess.Popen(cmd)
        out, _ = sp.communicate(stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print 'output from command: %s' % cmd
        print out
        return out
    except:
        print 'bad command: %s' % cmd
        tb.print_exc()
