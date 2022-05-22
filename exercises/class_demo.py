import re
import sys
import os



class interface:
    def __init__(self,name,ip,mask,status):
        self.name = name
        self.ip = ip
        self.mask = mask
        self.status = status
    def set_mtu(self,mtu):
        self.mtu = mtu

class router(interface):
    def __init__(self,router,name,ip,mask,status):
        self.router = router
        #interface.__init__(self,name,ip,mask,status)

int1 = router('r1','gig1','1.1.1.1','24','up')
print(dir(int1))