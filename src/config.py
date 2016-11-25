#coding=utf-8
'''
Created on Feb 1, 2016

@author: hualingson@foxmail.com
'''

from src import norm

__all__ = ['CMD_LIST_POOLS',
           'CMD_LIST_IMAGES_IN_POOL',
           'CMD_GRAB_BLOCK_NAME_PREFIX_SN',
           'CMD_FILTER_OBJECTS',
           'CMD_SHOW_OBJECT_PATH']

# come from ceph
# now regard:
#  rbd as block
#  rados as object
#  ceph as manager
#  todo: how to locate a file?

#ceph osd lspools
#3 master,6 test,
CMD_LIST_POOLS = ("ceph osd lspools", norm.compile("(\d+) (\w+),"))

#rbd -p poolname ls
#volume-28ad3623-100c-4da6-89cc-50db42426698
CMD_LIST_IMAGES_IN_POOL = ("rbd -p %(pool)s ls", norm.compile("(.+)\s+"))

#rbd -p poolname info imagename
#block_name_prefix: rbd_data.1791ce1a7a8c29
CMD_GRAB_BLOCK_NAME_PREFIX_SN = ("rbd -p %(pool)s info %(image)s", norm.compile("\s+block_name_prefix\: rbd_data\.(.+)\s+"))

#rbd -p poolname ls |grep 
#rbd_data.1d1ddc74b0dc51.0000000000000004
CMD_FILTER_OBJECTS = ("rados -p %(pool) ls |grep %(sn)s", norm.compile("(.+)\s+"))

#ceph osd map poolname objectname
#osdmap e3837 pool 'yangqiwen' (6) object 'rbd_data.1d1ddc74b0dc51.0000000000000000' -> pg 6.f3954aa4 (6.24) -> up ([2,1], p2) acting ([2,1], p2)
CMD_SHOW_OBJECT_PATH = ("ceph osd map %(pool)s %(object)s", norm.compile(" object .+\-\> pg.+\((.+)\) \-\> up \((.+), (.+)\) acting \((.+), (.+)\)"))
