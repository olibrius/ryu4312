# Copyright (C) 2012 Nippon Telegraph and Telephone Corporation.
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

# vim: tabstop=4 shiftwidth=4 softtabstop=4

import unittest
import logging
import struct
from struct import *
import pytest
from ryu.ofproto import ether, inet
from ryu.lib.packet.ethernet import ethernet
from ryu.lib.packet.packet import Packet
from ryu.lib.packet.ipv4 import ipv4
from ryu.lib.packet.vlan import vlan
from ryu.lib.packet.vlan import svlan


LOG = logging.getLogger('test_vlan')


class Test_vlan(unittest.TestCase):
    """ Test case for vlan
    """

    pcp = 0
    cfi = 0
    vid = 32
    tci = pcp << 15 | cfi << 12 | vid
    ethertype = ether.ETH_TYPE_IP

    buf = pack(vlan._PACK_STR, tci, ethertype)

    v = vlan(pcp, cfi, vid, ethertype)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def find_protocol(self, pkt, name):
        for p in pkt.protocols:
            if p.protocol_name == name:
                return p

    def test_init(self):
        assert self.pcp == self.v.pcp
        assert self.cfi == self.v.cfi
        assert self.vid == self.v.vid
        assert self.ethertype == self.v.ethertype
    def test_parser(self):
        res, ptype, _ = self.v.parser(self.buf)

        assert res.pcp == self.pcp
        assert res.cfi == self.cfi
        assert res.vid == self.vid
        assert res.ethertype == self.ethertype
        assert ptype == ipv4
    def test_serialize(self):
        data = bytearray()
        prev = None
        buf = self.v.serialize(data, prev)

        fmt = vlan._PACK_STR
        res = struct.unpack(fmt, buf)

        assert res[0] == self.tci
        assert res[1] == self.ethertype
    def _build_vlan(self):
        src_mac = '00:07:0d:af:f4:54'
        dst_mac = '00:00:00:00:00:00'
        ethertype = ether.ETH_TYPE_8021Q
        e = ethernet(dst_mac, src_mac, ethertype)

        version = 4
        header_length = 20
        tos = 0
        total_length = 24
        identification = 0x8a5d
        flags = 0
        offset = 1480
        ttl = 64
        proto = inet.IPPROTO_ICMP
        csum = 0xa7f2
        src = '131.151.32.21'
        dst = '131.151.32.129'
        option = b'TEST'
        ip = ipv4(version, header_length, tos, total_length, identification,
                  flags, offset, ttl, proto, csum, src, dst, option)

        p = Packet()

        p.add_protocol(e)
        p.add_protocol(self.v)
        p.add_protocol(ip)
        p.serialize()

        return p

    def test_build_vlan(self):
        p = self._build_vlan()

        e = self.find_protocol(p, "ethernet")
        assert e
        assert e.ethertype == ether.ETH_TYPE_8021Q
        v = self.find_protocol(p, "vlan")
        assert v
        assert v.ethertype == ether.ETH_TYPE_IP
        ip = self.find_protocol(p, "ipv4")
        assert ip
        assert v.pcp == self.pcp
        assert v.cfi == self.cfi
        assert v.vid == self.vid
        assert v.ethertype == self.ethertype
    @raises(Exception)
    def test_malformed_vlan(self):
        m_short_buf = self.buf[1:vlan._MIN_LEN]
        vlan.parser(m_short_buf)

    def test_json(self):
        jsondict = self.v.to_jsondict()
        v = vlan.from_jsondict(jsondict['vlan'])
        assert str(self.v) == str(v)
class Test_svlan(unittest.TestCase):

    pcp = 0
    cfi = 0
    vid = 32
    tci = pcp << 15 | cfi << 12 | vid
    ethertype = ether.ETH_TYPE_8021Q

    buf = pack(svlan._PACK_STR, tci, ethertype)

    sv = svlan(pcp, cfi, vid, ethertype)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def find_protocol(self, pkt, name):
        for p in pkt.protocols:
            if p.protocol_name == name:
                return p

    def test_init(self):
        assert self.pcp == self.sv.pcp
        assert self.cfi == self.sv.cfi
        assert self.vid == self.sv.vid
        assert self.ethertype == self.sv.ethertype
    def test_parser(self):
        res, ptype, _ = self.sv.parser(self.buf)

        assert res.pcp == self.pcp
        assert res.cfi == self.cfi
        assert res.vid == self.vid
        assert res.ethertype == self.ethertype
        assert ptype == vlan
    def test_serialize(self):
        data = bytearray()
        prev = None
        buf = self.sv.serialize(data, prev)

        fmt = svlan._PACK_STR
        res = struct.unpack(fmt, buf)

        assert res[0] == self.tci
        assert res[1] == self.ethertype
    def _build_svlan(self):
        src_mac = '00:07:0d:af:f4:54'
        dst_mac = '00:00:00:00:00:00'
        ethertype = ether.ETH_TYPE_8021AD
        e = ethernet(dst_mac, src_mac, ethertype)

        pcp = 0
        cfi = 0
        vid = 32
        tci = pcp << 15 | cfi << 12 | vid
        ethertype = ether.ETH_TYPE_IP
        v = vlan(pcp, cfi, vid, ethertype)

        version = 4
        header_length = 20
        tos = 0
        total_length = 24
        identification = 0x8a5d
        flags = 0
        offset = 1480
        ttl = 64
        proto = inet.IPPROTO_ICMP
        csum = 0xa7f2
        src = '131.151.32.21'
        dst = '131.151.32.129'
        option = b'TEST'
        ip = ipv4(version, header_length, tos, total_length, identification,
                  flags, offset, ttl, proto, csum, src, dst, option)

        p = Packet()

        p.add_protocol(e)
        p.add_protocol(self.sv)
        p.add_protocol(v)
        p.add_protocol(ip)
        p.serialize()

        return p

    def test_build_svlan(self):
        p = self._build_svlan()

        e = self.find_protocol(p, "ethernet")
        assert e
        assert e.ethertype == ether.ETH_TYPE_8021AD
        sv = self.find_protocol(p, "svlan")
        assert sv
        assert sv.ethertype == ether.ETH_TYPE_8021Q
        v = self.find_protocol(p, "vlan")
        assert v
        assert v.ethertype == ether.ETH_TYPE_IP
        ip = self.find_protocol(p, "ipv4")
        assert ip
        assert sv.pcp == self.pcp
        assert sv.cfi == self.cfi
        assert sv.vid == self.vid
        assert sv.ethertype == self.ethertype
    @raises(Exception)
    def test_malformed_svlan(self):
        m_short_buf = self.buf[1:svlan._MIN_LEN]
        svlan.parser(m_short_buf)

    def test_json(self):
        jsondict = self.sv.to_jsondict()
        sv = svlan.from_jsondict(jsondict['svlan'])
        assert str(self.sv) == str(sv)