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
import six
import struct
from struct import *
import pytest
from ryu.ofproto import ether, inet
from ryu.lib.packet import packet_utils
from ryu.lib.packet.ethernet import ethernet
from ryu.lib.packet.packet import Packet
from ryu.lib.packet.ipv4 import ipv4
from ryu.lib.packet.tcp import tcp
from ryu.lib import addrconv


LOG = logging.getLogger('test_ipv4')


class Test_ipv4(unittest.TestCase):
    """ Test case for ipv4
    """

    version = 4
    header_length = 5 + 10
    ver_hlen = version << 4 | header_length
    tos = 0
    total_length = header_length + 64
    identification = 30774
    flags = 4
    offset = 1480
    flg_off = flags << 13 | offset
    ttl = 64
    proto = inet.IPPROTO_TCP
    csum = 0xadc6
    src = '131.151.32.21'
    dst = '131.151.32.129'
    length = header_length * 4
    option = b'\x86\x28\x00\x00\x00\x01\x01\x22' \
        + b'\x00\x01\xae\x00\x00\x00\x00\x00' \
        + b'\x00\x00\x00\x00\x00\x00\x00\x00' \
        + b'\x00\x00\x00\x00\x00\x00\x00\x00' \
        + b'\x00\x00\x00\x00\x00\x00\x00\x01'

    buf = pack(ipv4._PACK_STR, ver_hlen, tos, total_length, identification,
               flg_off, ttl, proto, csum,
               addrconv.ipv4.text_to_bin(src),
               addrconv.ipv4.text_to_bin(dst)) \
        + option

    ip = ipv4(version, header_length, tos, total_length, identification,
              flags, offset, ttl, proto, csum, src, dst, option)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        assert self.version == self.ip.version
        assert self.header_length == self.ip.header_length
        assert self.tos == self.ip.tos
        assert self.total_length == self.ip.total_length
        assert self.identification == self.ip.identification
        assert self.flags == self.ip.flags
        assert self.offset == self.ip.offset
        assert self.ttl == self.ip.ttl
        assert self.proto == self.ip.proto
        assert self.csum == self.ip.csum
        assert self.src == self.ip.src
        assert self.dst == self.ip.dst
        assert self.length == len(self.ip)
        assert self.option == self.ip.option
    def test_parser(self):
        res, ptype, _ = self.ip.parser(self.buf)

        assert res.version == self.version
        assert res.header_length == self.header_length
        assert res.tos == self.tos
        assert res.total_length == self.total_length
        assert res.identification == self.identification
        assert res.flags == self.flags
        assert res.offset == self.offset
        assert res.ttl == self.ttl
        assert res.proto == self.proto
        assert res.csum == self.csum
        assert res.src == self.src
        assert res.dst == self.dst
        assert ptype == tcp
    def test_serialize(self):
        buf = self.ip.serialize(bytearray(), None)
        res = struct.unpack_from(ipv4._PACK_STR, six.binary_type(buf))
        option = buf[ipv4._MIN_LEN:ipv4._MIN_LEN + len(self.option)]

        assert res[0] == self.ver_hlen
        assert res[1] == self.tos
        assert res[2] == self.total_length
        assert res[3] == self.identification
        assert res[4] == self.flg_off
        assert res[5] == self.ttl
        assert res[6] == self.proto
        assert res[8] == addrconv.ipv4.text_to_bin(self.src)
        assert res[9] == addrconv.ipv4.text_to_bin(self.dst)
        assert option == self.option
        # checksum
        csum = packet_utils.checksum(buf)
        assert csum == 0
    def test_malformed_ipv4(self):
        with pytest.raises(Exception):
            m_short_buf = self.buf[1:ipv4._MIN_LEN]
            ipv4.parser(m_short_buf)

    def test_json(self):
        jsondict = self.ip.to_jsondict()
        ip = ipv4.from_jsondict(jsondict['ipv4'])
        assert str(self.ip) == str(ip)