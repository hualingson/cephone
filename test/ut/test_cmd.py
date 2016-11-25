#coding=utf-8
'''
Created on Feb 1, 2016

@author: hualingson@foxmail.com
'''

from test.ut import TestCephOnly
from src.cmd import *

class TestCmd(TestCephOnly):
    
    def _test(self, cmd_mac, response):
        '_test.__doc__'
        cmd, mac = cmd_mac
        print 'command:', cmd
        result = mac.findall(response)
        print 'response:', response
        print 'result:', result
        return result
    
    def test_list_pools(self):
        '3 master,6 test,'
        self._test(CMD_LIST_POOLS, self.test_list_pools.__doc__)
    
    def test_list_images(self):
        '''9a473f1f-6963-40e7-bce6-19f05dcc9e60_disk
9ee2faed-d3c1-447e-9eb4-0bb73067018c_disk
ab79e9e1-375f-4bda-ae89-1dcbdd708a01
c79ab372-0325-4ebe-a53d-6f71e895a2f6
da1a0d09-e35c-4f04-88fb-8d0a91269155_disk
f0925dbc-9ba3-41cf-bb02-7492809934fd
volume-07c6c631-dde4-4aa3-b227-6f3442d9ac08
volume-12475405-0116-49b5-ba3d-ef84606e3c61
volume-1cb22903-db77-43e6-9656-fa997e87eef5
volume-1e18374a-e913-4003-862a-f7cef05311f8
volume-20a701b1-cf6b-4cb5-bb04-1a5aef93e84e
volume-24890586-9056-42d7-bad5-2f80dc448649.deleted
volume-28ad3623-100c-4da6-89cc-50db42426698
volume-386078b2-7e6f-459d-986d-19109f07c3a4
volume-38766829-f462-4920-b6e3-f1b4d215a3ec
volume-3c3515b8-4b7f-4003-b96e-cd46c2fd5292
volume-44b26ada-f307-41b1-8600-82d0ef94565f.backup.base
volume-4d4a1f08-b741-4360-897c-44c7122de4f3
volume-4d4a1f08-b741-4360-897c-44c7122de4f3.backup.base
volume-67146a7d-9d27-42cb-ba6a-fe00b813083f
volume-6f8726b5-4994-48ed-9309-cf077c9b78f0.deleted
volume-791d60a2-de38-47d0-bc31-3cd3517362da.deleted
volume-8750ebf2-69ed-411b-8334-451cce7ebe30
volume-a1ae428e-5899-4148-8da2-e9d67d1fc685
volume-b1789a52-f17c-4c59-a14d-08fd4ceeb13d
volume-b712b144-b545-4e1b-87ab-2b0ae0f4a33e
volume-e1f6c805-ee07-4c25-adf4-aad50eef640e
volume-f34468a5-f7f4-4c62-8659-8bf6f5964842.deleted
volume-f4c7b7f1-7eac-41cf-8b03-7b13cc3aafc3'''
        self._test(CMD_LIST_IMAGES_IN_POOL, self.test_list_images.__doc__)
    
    def test_list_blocks(self):
        '''
        rbd image 'ab79e9e1-375f-4bda-ae89-1dcbdd708a01':
            size 9532 kB in 2 objects
            order 23 (8192 kB objects)
            block_name_prefix: rbd_data.1791ce1a7a8c29
            format: 2
            features: layering
            flags:
        '''
        self._test(CMD_GRAB_BLOCK_NAME_PREFIX_SN, self.test_list_blocks.__doc__)
    
    def test_list_objects(self):
        '''rbd_data.1d1ddc74b0dc51.0000000000000001
rbd_data.1d1ddc74b0dc51.0000000000000007
rbd_header.1d1ddc74b0dc51
rbd_data.1d1ddc74b0dc51.0000000000000002
rbd_data.1d1ddc74b0dc51.0000000000000000
rbd_data.1d1ddc74b0dc51.0000000000000006
rbd_data.1d1ddc74b0dc51.0000000000000003
rbd_data.1d1ddc74b0dc51.0000000000000005
rbd_data.1d1ddc74b0dc51.0000000000000004'''
        self._test(CMD_FILTER_OBJECTS, self.test_list_objects.__doc__)
    
    def test_list_paths(self):
        '''2016-02-02 18:51:14.362371 7ffbac611700  0 -- :/1017309 >> 10.10.3.162:6789/0 pipe(0x7ffba80282c0 sd=3 :0 s=1 pgs=0 cs=0 l=1 c=0x7ffba8024380).fault
osdmap e3837 pool 'yangqiwen' (6) object 'rbd_data.1d1ddc74b0dc51.0000000000000000' -> pg 6.f3954aa4 (6.24) -> up ([2,1], p2) acting ([2,1], p2)'''
        result = self._test(CMD_SHOW_OBJECT_PATH, self.test_list_paths.__doc__)
        pg, up_order, up_point, acting_order, acting_point = result[0]
        self.assertEqual(pg, '6.24', 'pg')
        self.assertEqual(eval(up_order), [2,1], 'up order')
        self.assertEqual(up_point, 'p2', 'up point')
        self.assertEqual(eval(acting_order), [2,1], 'acting order')
        self.assertEqual(acting_point, 'p2', 'acting point')
