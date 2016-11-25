#coding=utf-8
'''
Created on Feb 23, 2016

@author: hualingson@foxmail.com
'''

import rbd
import rados

if __name__ == '__main__':
    ceph_conf = '/root/ceph/src/ceph.conf'
    cluster = rados.Rados(conffile=ceph_conf)
    cluster.connect(5)
    from src import pp
    pp.pprint(cluster.get_cluster_stats())
    cluster.shutdown()
