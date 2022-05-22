from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
import threading, time
import json
import os
import sys
import signal

import threading, time


class PerfSwitch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(PerfSwitch, self).__init__(*args, **kwargs)
        self.mac_to_port = {}
        print(True)

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        print(True)
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        print('before dpid')
        dpid = datapath.id
        print(dpid)
        print('after dpid')
        self.start = time.time()
        self.flow_count = 0
        mac_int = 77846282242
        mac_int = 77846282242 # 00:12:20:00:00:00 Give 00:12:20:00:00:02 in spirent or ixia as start mac
        ofport=25
        in_port = 22
        for in_port in [21,22,23,24,25]:
            for x in range(1):
                print(x)
                pri = x + 10
                mac_hex = "{:012x}".format(mac_int)
                mac_str = ":".join(mac_hex[i:i+2] for i in range(0, len(mac_hex), 2))
                print(mac_str)
                match = parser.OFPMatch(in_port=in_port)
                #actions = [parser.OFPActionOutput(ofport)]
                #inst=[parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]
                inst = [parser.OFPInstructionGotoTable(8)]
    #            print('inst')
                mod = parser.OFPFlowMod(datapath, table_id=0,command=ofproto.OFPFC_ADD, priority=pri, cookie=(10000), match=match, instructions=inst)
    #            print(mod)
                datapath.send_msg(mod)
                self.flow_count += 1
                mac_int += 1
        req = parser.OFPBarrierRequest(datapath)
        datapath.send_msg(req)
        self.barrier = time.time()

    @set_ev_cls(ofp_event.EventOFPBarrierReply, MAIN_DISPATCHER)
    def _barrier_reply(self, ev):
        now = time.time()
        print ("Install %d flows" % self.flow_count)
        print ("Time taken between Barrier Request and Reply in Sec: %0.05f" % (now - self.barrier))
        print ("Time taken between Start and Barrier Reply in Sec: %0.05f" % (now - self.start))
        print ("Flows/sec is : %0.0f" % (self.flow_count / (now - self.start)))
        os._exit(0)





# Copyright (C) 2011 Nippon Telegraph and Telephone Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
import threading, time
import json
import os
import sys
import signal

import threading, time


class PerfSwitch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(PerfSwitch, self).__init__(*args, **kwargs)
        self.mac_to_port = {}
        print(True)

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        print(True)
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        print(True)
        self.start = time.time()
        self.flow_count = 0
        out_port = [21,22,23,24]
        in_port = 25
        vlan_list = [100,200,300,400]

        for port,vlan in zip(out_port,vlan_list):
            for t_id in range (1):
                t_id = 0
                for pri in range(1):
                    print(pri)
                    match = parser.OFPMatch(in_port=in_port)
                    #match = parser.OFPMatch()
                    match = parser.OFPMatch(in_port=in_port, vlan_vid=vlan)
                    actions = [parser.OFPActionOutput(port)]
                    inst=[parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]
                    print('before inst')
                    #inst = [parser.OFPInstructionGotoTable(1)]
                    print('before mod')
                    mod = parser.OFPFlowMod(datapath, table_id=t_id, command=ofproto.OFPFC_ADD, priority=(1), cookie=(10000), match=match, instructions=inst)
                    datapath.send_msg(mod)
                    self.flow_count += 1

        req = parser.OFPBarrierRequest(datapath)
        datapath.send_msg(req)
        self.barrier = time.time()

    @set_ev_cls(ofp_event.EventOFPBarrierReply, MAIN_DISPATCHER)
    def _barrier_reply(self, ev):
        now = time.time()
        print ("Install %d flows" % self.flow_count)
        print ("Time taken between Barrier Request and Reply in Sec: %0.05f" % (now - self.barrier))
        print ("Time taken between Start and Barrier Reply in Sec: %0.05f" % (now - self.start))
        print ("Flows/sec is : %0.0f" % (self.flow_count / (now - self.start)))
        os._exit(0)




from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
import threading, time
import json
import os
import sys
import signal

import threading, time


class PerfSwitch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(PerfSwitch, self).__init__(*args, **kwargs)
        self.mac_to_port = {}
        print(True)

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        print(True)
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        print('before dpid')
        dpid = datapath.id
        print(dpid)
        print('after dpid')
        self.start = time.time()
        self.flow_count = 0
        mac_int = 77846282242
        mac_int = 77846282242 # 00:12:20:00:00:00 Give 00:12:20:00:00:02 in spirent or ixia as start mac
        ofport=25
        in_port = 22
        for in_port in [21,22,23,24]:
            mac_int = 77846282242
            if in_port == 21:
                total_mac = 4890
            else:
                total_mac = 4891
            for x in range(total_mac):
                print(x)
                pri = x + 10
                mac_hex = "{:012x}".format(mac_int)
                mac_str = ":".join(mac_hex[i:i+2] for i in range(0, len(mac_hex), 2))
                print(mac_str)
                match = parser.OFPMatch(in_port=in_port,eth_src=mac_str)
                actions = [parser.OFPActionOutput(ofport)]
                inst=[parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]
                #inst = [parser.OFPInstructionGotoTable(8)]
    #            print('inst')
                mod = parser.OFPFlowMod(datapath, table_id=0,command=ofproto.OFPFC_ADD, priority=pri, cookie=(10000), match=match, instructions=inst)
    #            print(mod)
                datapath.send_msg(mod)
                self.flow_count += 1
                mac_int += 1
        req = parser.OFPBarrierRequest(datapath)
        datapath.send_msg(req)
        self.barrier = time.time()

    @set_ev_cls(ofp_event.EventOFPBarrierReply, MAIN_DISPATCHER)
    def _barrier_reply(self, ev):
        now = time.time()
        print ("Install %d flows" % self.flow_count)
        print ("Time taken between Barrier Request and Reply in Sec: %0.05f" % (now - self.barrier))
        print ("Time taken between Start and Barrier Reply in Sec: %0.05f" % (now - self.start))
        print ("Flows/sec is : %0.0f" % (self.flow_count / (now - self.start)))
        os._exit(0)
