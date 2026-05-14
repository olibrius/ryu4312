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
from ryu.ofproto.ofproto_v1_2 import *


LOG = logging.getLogger('test_ofproto_v12')


class TestOfprot12(unittest.TestCase):
    """ Test case for ofproto_v1_2
    """

    def test_struct_ofp_header(self):
        assert OFP_HEADER_PACK_STR == '!BBHI'
        assert OFP_HEADER_SIZE == 8
    def test_enum_ofp_type(self):
        assert OFPT_HELLO == 0
        assert OFPT_ERROR == 1
        assert OFPT_ECHO_REQUEST == 2
        assert OFPT_ECHO_REPLY == 3
        assert OFPT_EXPERIMENTER == 4
        assert OFPT_FEATURES_REQUEST == 5
        assert OFPT_FEATURES_REPLY == 6
        assert OFPT_GET_CONFIG_REQUEST == 7
        assert OFPT_GET_CONFIG_REPLY == 8
        assert OFPT_SET_CONFIG == 9
        assert OFPT_PACKET_IN == 10
        assert OFPT_FLOW_REMOVED == 11
        assert OFPT_PORT_STATUS == 12
        assert OFPT_PACKET_OUT == 13
        assert OFPT_FLOW_MOD == 14
        assert OFPT_GROUP_MOD == 15
        assert OFPT_PORT_MOD == 16
        assert OFPT_TABLE_MOD == 17
        assert OFPT_STATS_REQUEST == 18
        assert OFPT_STATS_REPLY == 19
        assert OFPT_BARRIER_REQUEST == 20
        assert OFPT_BARRIER_REPLY == 21
        assert OFPT_QUEUE_GET_CONFIG_REQUEST == 22
        assert OFPT_QUEUE_GET_CONFIG_REPLY == 23
        assert OFPT_ROLE_REQUEST == 24
        assert OFPT_ROLE_REPLY == 25
    def test_struct_ofp_port(self):
        assert OFP_PORT_PACK_STR == '!I4x6s2x16sIIIIIIII'
        assert OFP_PORT_SIZE == 64
    def test_enum_ofp_port_config(self):
        assert OFPPC_PORT_DOWN == 1 << 0
        assert OFPPC_NO_RECV == 1 << 2
        assert OFPPC_NO_FWD == 1 << 5
        assert OFPPC_NO_PACKET_IN == 1 << 6
    def test_enum_ofp_port_state(self):
        assert OFPPS_LINK_DOWN == 1 << 0
        assert OFPPS_BLOCKED == 1 << 1
        assert OFPPS_LIVE == 1 << 2
    def test_enum_ofp_port_no(self):
        assert OFPP_MAX == 0xffffff00
        assert OFPP_IN_PORT == 0xfffffff8
        assert OFPP_TABLE == 0xfffffff9
        assert OFPP_NORMAL == 0xfffffffa
        assert OFPP_FLOOD == 0xfffffffb
        assert OFPP_ALL == 0xfffffffc
        assert OFPP_CONTROLLER == 0xfffffffd
        assert OFPP_LOCAL == 0xfffffffe
        assert OFPP_ANY == 0xffffffff
        assert OFPQ_ALL == 0xffffffff
    def test_enum_ofp_port_features(self):
        assert OFPPF_10MB_HD == 1 << 0
        assert OFPPF_10MB_FD == 1 << 1
        assert OFPPF_100MB_HD == 1 << 2
        assert OFPPF_100MB_FD == 1 << 3
        assert OFPPF_1GB_HD == 1 << 4
        assert OFPPF_1GB_FD == 1 << 5
        assert OFPPF_10GB_FD == 1 << 6
        assert OFPPF_40GB_FD == 1 << 7
        assert OFPPF_100GB_FD == 1 << 8
        assert OFPPF_1TB_FD == 1 << 9
        assert OFPPF_OTHER == 1 << 10
        assert OFPPF_COPPER == 1 << 11
        assert OFPPF_FIBER == 1 << 12
        assert OFPPF_AUTONEG == 1 << 13
        assert OFPPF_PAUSE == 1 << 14
        assert OFPPF_PAUSE_ASYM == 1 << 15
    def test_struct_ofp_packet_queue(self):
        assert OFP_PACKET_QUEUE_PACK_STR == '!IIH6x'
        assert OFP_PACKET_QUEUE_SIZE == 16
    def test_enum_ofp_queue_properties(self):
        assert OFPQT_MIN_RATE == 1
        assert OFPQT_MAX_RATE == 2
        assert OFPQT_EXPERIMENTER == 0xffff
    def test_struct_ofp_queue_prop_header(self):
        assert OFP_QUEUE_PROP_HEADER_PACK_STR == '!HH4x'
        assert OFP_QUEUE_PROP_HEADER_SIZE == 8
    def test_struct_ofp_queue_prop_min_rate(self):
        assert OFP_QUEUE_PROP_MIN_RATE_PACK_STR == '!H6x'
        assert OFP_QUEUE_PROP_MIN_RATE_SIZE == 16
    def test_struct_ofp_queue_prop_max_rate(self):
        assert OFP_QUEUE_PROP_MAX_RATE_PACK_STR == '!H6x'
        assert OFP_QUEUE_PROP_MAX_RATE_SIZE == 16
    def test_struct_ofp_queue_prop_experimenter(self):
        assert OFP_QUEUE_PROP_EXPERIMENTER_PACK_STR == '!I4x'
        assert OFP_QUEUE_PROP_EXPERIMENTER_SIZE == 16
    def test_struct_ofp_match(self):
        assert OFP_MATCH_PACK_STR == '!HHBBBB'
        assert OFP_MATCH_SIZE == 8
    def test_enum_ofp_match_type(self):
        assert OFPMT_STANDARD == 0
        assert OFPMT_OXM == 1
    def test_enum_ofp_oxm_class(self):
        assert OFPXMC_NXM_0 == 0x0000
        assert OFPXMC_NXM_1 == 0x0001
        assert OFPXMC_OPENFLOW_BASIC == 0x8000
        assert OFPXMC_EXPERIMENTER == 0xFFFF
    def test_enmu_oxm_ofb_match_fields(self):
        assert OFPXMT_OFB_IN_PORT == 0
        assert OFPXMT_OFB_IN_PHY_PORT == 1
        assert OFPXMT_OFB_METADATA == 2
        assert OFPXMT_OFB_ETH_DST == 3
        assert OFPXMT_OFB_ETH_SRC == 4
        assert OFPXMT_OFB_ETH_TYPE == 5
        assert OFPXMT_OFB_VLAN_VID == 6
        assert OFPXMT_OFB_VLAN_PCP == 7
        assert OFPXMT_OFB_IP_DSCP == 8
        assert OFPXMT_OFB_IP_ECN == 9
        assert OFPXMT_OFB_IP_PROTO == 10
        assert OFPXMT_OFB_IPV4_SRC == 11
        assert OFPXMT_OFB_IPV4_DST == 12
        assert OFPXMT_OFB_TCP_SRC == 13
        assert OFPXMT_OFB_TCP_DST == 14
        assert OFPXMT_OFB_UDP_SRC == 15
        assert OFPXMT_OFB_UDP_DST == 16
        assert OFPXMT_OFB_SCTP_SRC == 17
        assert OFPXMT_OFB_SCTP_DST == 18
        assert OFPXMT_OFB_ICMPV4_TYPE == 19
        assert OFPXMT_OFB_ICMPV4_CODE == 20
        assert OFPXMT_OFB_ARP_OP == 21
        assert OFPXMT_OFB_ARP_SPA == 22
        assert OFPXMT_OFB_ARP_TPA == 23
        assert OFPXMT_OFB_ARP_SHA == 24
        assert OFPXMT_OFB_ARP_THA == 25
        assert OFPXMT_OFB_IPV6_SRC == 26
        assert OFPXMT_OFB_IPV6_DST == 27
        assert OFPXMT_OFB_IPV6_FLABEL == 28
        assert OFPXMT_OFB_ICMPV6_TYPE == 29
        assert OFPXMT_OFB_ICMPV6_CODE == 30
        assert OFPXMT_OFB_IPV6_ND_TARGET == 31
        assert OFPXMT_OFB_IPV6_ND_SLL == 32
        assert OFPXMT_OFB_IPV6_ND_TLL == 33
        assert OFPXMT_OFB_MPLS_LABEL == 34
        assert OFPXMT_OFB_MPLS_TC == 35
    def test_enum_ofp_vlan_id(self):
        assert OFPVID_PRESENT == 0x1000
        assert OFPVID_NONE == 0x0000
    def test_struct_ofp_oxm_experimenter_header(self):
        assert OFP_OXM_EXPERIMENTER_HEADER_PACK_STR == '!II'
        assert OFP_OXM_EXPERIMENTER_HEADER_SIZE == 8
    def test_enum_ofp_instruction_type(self):
        assert OFPIT_GOTO_TABLE == 1
        assert OFPIT_WRITE_METADATA == 2
        assert OFPIT_WRITE_ACTIONS == 3
        assert OFPIT_APPLY_ACTIONS == 4
        assert OFPIT_CLEAR_ACTIONS == 5
        assert OFPIT_EXPERIMENTER == 0xFFFF
    def test_struct_ofp_instruction_goto_table(self):
        assert OFP_INSTRUCTION_GOTO_TABLE_PACK_STR == '!HHB3x'
        assert OFP_INSTRUCTION_GOTO_TABLE_SIZE == 8
    def test_struct_ofp_instruction_write_metadata(self):
        assert OFP_INSTRUCTION_WRITE_METADATA_PACK_STR == '!HH4xQQ'
        assert OFP_INSTRUCTION_WRITE_METADATA_SIZE == 24
    def test_struct_ofp_instaruction_actions(self):
        assert OFP_INSTRUCTION_ACTIONS_PACK_STR == '!HH4x'
        assert OFP_INSTRUCTION_ACTIONS_SIZE == 8
    def test_enum_ofp_action_type(self):
        assert OFPAT_OUTPUT == 0
        assert OFPAT_COPY_TTL_OUT == 11
        assert OFPAT_COPY_TTL_IN == 12
        assert OFPAT_SET_MPLS_TTL == 15
        assert OFPAT_DEC_MPLS_TTL == 16
        assert OFPAT_PUSH_VLAN == 17
        assert OFPAT_POP_VLAN == 18
        assert OFPAT_PUSH_MPLS == 19
        assert OFPAT_POP_MPLS == 20
        assert OFPAT_SET_QUEUE == 21
        assert OFPAT_GROUP == 22
        assert OFPAT_SET_NW_TTL == 23
        assert OFPAT_DEC_NW_TTL == 24
        assert OFPAT_SET_FIELD == 25
        assert OFPAT_EXPERIMENTER == 0xffff
    def test_struct_ofp_action_header(self):
        assert OFP_ACTION_HEADER_PACK_STR == '!HH4x'
        assert OFP_ACTION_HEADER_SIZE == 8
    def test_struct_ofp_action_output(self):
        assert OFP_ACTION_OUTPUT_PACK_STR == '!HHIH6x'
        assert OFP_ACTION_OUTPUT_SIZE == 16
    def test_enum_ofp_controller_max_len(self):
        assert OFPCML_MAX == 0xffe5
        assert OFPCML_NO_BUFFER == 0xffff
    def test_struct_ofp_action_group(self):
        assert OFP_ACTION_GROUP_PACK_STR == '!HHI'
        assert OFP_ACTION_GROUP_SIZE == 8
    def test_struct_ofp_action_set_queue(self):
        assert OFP_ACTION_SET_QUEUE_PACK_STR == '!HHI'
        assert OFP_ACTION_SET_QUEUE_SIZE == 8
    def test_struct_ofp_aciton_mpls_ttl(self):
        assert OFP_ACTION_MPLS_TTL_PACK_STR == '!HHB3x'
        assert OFP_ACTION_MPLS_TTL_SIZE == 8
    def test_struct_ofp_action_nw_ttl(self):
        assert OFP_ACTION_NW_TTL_PACK_STR == '!HHB3x'
        assert OFP_ACTION_NW_TTL_SIZE == 8
    def test_struct_ofp_action_push(self):
        assert OFP_ACTION_PUSH_PACK_STR == '!HHH2x'
        assert OFP_ACTION_PUSH_SIZE == 8
    def test_struct_ofp_action_pop_mpls(self):
        assert OFP_ACTION_POP_MPLS_PACK_STR == '!HHH2x'
        assert OFP_ACTION_POP_MPLS_SIZE == 8
    def test_struct_ofp_action_set_field(self):
        assert OFP_ACTION_SET_FIELD_PACK_STR == '!HH4B'
        assert OFP_ACTION_SET_FIELD_SIZE == 8
    def test_struct_ofp_action_experimenter_header(self):
        assert OFP_ACTION_EXPERIMENTER_HEADER_PACK_STR == '!HHI'
        assert OFP_ACTION_EXPERIMENTER_HEADER_SIZE == 8
    def test_struct_ofp_switch_feature(self):
        assert OFP_SWITCH_FEATURES_PACK_STR == '!QIB3xII'
        assert OFP_SWITCH_FEATURES_SIZE == 32
    def test_enum_ofp_capabilities(self):
        assert OFPC_FLOW_STATS == 1 << 0
        assert OFPC_TABLE_STATS == 1 << 1
        assert OFPC_PORT_STATS == 1 << 2
        assert OFPC_GROUP_STATS == 1 << 3
        assert OFPC_IP_REASM == 1 << 5
        assert OFPC_QUEUE_STATS == 1 << 6
        assert OFPC_PORT_BLOCKED == 1 << 8
    def test_struct_ofp_switch_config(self):
        assert OFP_SWITCH_CONFIG_PACK_STR == '!HH'
        assert OFP_SWITCH_CONFIG_SIZE == 12
    def test_enum_ofp_config_flags(self):
        assert OFPC_FRAG_NORMAL == 0
        assert OFPC_FRAG_DROP == 1 << 0
        assert OFPC_FRAG_REASM == 1 << 1
        assert OFPC_FRAG_MASK == 3
        assert OFPC_INVALID_TTL_TO_CONTROLLER == 1 << 2
    def test_enum_ofp_table(self):
        assert OFPTT_MAX == 0xfe
        assert OFPTT_ALL == 0xff
    def test_struct_ofp_table_mod(self):
        assert OFP_TABLE_MOD_PACK_STR == '!B3xI'
        assert OFP_TABLE_MOD_SIZE == 16
    def test_enum_ofp_table_config(self):
        assert OFPTC_TABLE_MISS_CONTROLLER == 0
        assert OFPTC_TABLE_MISS_CONTINUE == 1 << 0
        assert OFPTC_TABLE_MISS_DROP == 1 << 1
        assert OFPTC_TABLE_MISS_MASK == 3
    def test_struct_ofp_flow_mod(self):
        assert OFP_FLOW_MOD_PACK_STR == '!QQBBHHHIIIH2xHHBBBB'
        assert OFP_FLOW_MOD_SIZE == 56
    def test_enum_ofp_flow_mod_command(self):
        assert OFPFC_ADD == 0
        assert OFPFC_MODIFY == 1
        assert OFPFC_MODIFY_STRICT == 2
        assert OFPFC_DELETE == 3
        assert OFPFC_DELETE_STRICT == 4
    def test_enum_ofp_flow_mod_flags(self):
        assert OFPFF_SEND_FLOW_REM == 1 << 0
        assert OFPFF_CHECK_OVERLAP == 1 << 1
        assert OFPFF_RESET_COUNTS == 1 << 2
    def test_struct_ofp_group_mod(self):
        assert OFP_GROUP_MOD_PACK_STR == '!HBxI'
        assert OFP_GROUP_MOD_SIZE == 16
    # same to OFPP_*
    def test_enum_ofp_group(self):
        assert OFPG_MAX == 0xffffff00
        assert OFPG_ALL == 0xfffffffc
        assert OFPG_ANY == 0xffffffff
    def test_enum_ofp_group_mod_command(self):
        assert OFPGC_ADD == 0
        assert OFPGC_MODIFY == 1
        assert OFPGC_DELETE == 2
    def test_enum_ofp_group_type(self):
        assert OFPGT_ALL == 0
        assert OFPGT_SELECT == 1
        assert OFPGT_INDIRECT == 2
        assert OFPGT_FF == 3
    def test_struct_ofp_bucket(self):
        assert OFP_BUCKET_PACK_STR == '!HHII4x'
        assert OFP_BUCKET_SIZE == 16
    def test_struct_ofp_port_mod(self):
        assert OFP_PORT_MOD_PACK_STR == '!I4x6s2xIII4x'
        assert OFP_PORT_MOD_SIZE == 40
    def test_sturct_ofp_stats_request(self):
        assert OFP_STATS_REQUEST_PACK_STR == '!HH4x'
        assert OFP_STATS_REQUEST_SIZE == 16
    # OFPSF_REQ_* flags (none yet defined).
    # The only value defined for flags in a reply is whether more
    # replies will follow this one - this has the value 0x0001.
    def test_enum_ofp_stats_reply_flags(self):
        assert OFPSF_REPLY_MORE == 0x0001
    def test_struct_ofp_stats_reply(self):
        assert OFP_STATS_REPLY_PACK_STR == '!HH4x'
        assert OFP_STATS_REPLY_SIZE == 16
    def test_enum_ofp_stats_types(self):
        assert OFPST_DESC == 0
        assert OFPST_FLOW == 1
        assert OFPST_AGGREGATE == 2
        assert OFPST_TABLE == 3
        assert OFPST_PORT == 4
        assert OFPST_QUEUE == 5
        assert OFPST_GROUP == 6
        assert OFPST_GROUP_DESC == 7
        assert OFPST_GROUP_FEATURES == 8
        assert OFPST_EXPERIMENTER == 0xffff
    def test_struct_ofp_desc_stats(self):
        assert OFP_DESC_STATS_PACK_STR == '!256s256s256s32s256s'
        assert OFP_DESC_STATS_SIZE == 1056
    def test_struct_ofp_flow_stats_request(self):
        assert OFP_FLOW_STATS_REQUEST_PACK_STR == '!B3xII4xQQ'
        assert OFP_FLOW_STATS_REQUEST_SIZE == 40
    def test_struct_ofp_flow_stats(self):
        assert OFP_FLOW_STATS_PACK_STR == '!HBxIIHHH6xQQQ'
        assert OFP_FLOW_STATS_SIZE == 56
    def test_struct_ofp_aggregate_stats_request(self):
        assert OFP_AGGREGATE_STATS_REQUEST_PACK_STR == '!B3xII4xQQ'
        assert OFP_AGGREGATE_STATS_REQUEST_SIZE == 40
    def test_struct_ofp_aggregate_stats_reply(self):
        assert OFP_AGGREGATE_STATS_REPLY_PACK_STR == '!QQI4x'
        assert OFP_AGGREGATE_STATS_REPLY_SIZE == 24
    def test_sturct_ofp_table_stats(self):
        assert OFP_TABLE_STATS_PACK_STR == '!B7x32sQQIIQQQQIIIIQQ'
        assert OFP_TABLE_STATS_SIZE == 128
    def test_struct_ofp_port_stats_request(self):
        assert OFP_PORT_STATS_REQUEST_PACK_STR == '!I4x'
        assert OFP_PORT_STATS_REQUEST_SIZE == 8
    def test_struct_ofp_port_stats(self):
        assert OFP_PORT_STATS_PACK_STR == '!I4xQQQQQQQQQQQQ'
        assert OFP_PORT_STATS_SIZE == 104
    def test_struct_ofp_queue_stats_request(self):
        assert OFP_QUEUE_STATS_REQUEST_PACK_STR == '!II'
        assert OFP_QUEUE_STATS_REQUEST_SIZE == 8
    def test_struct_ofp_queue_stats(self):
        assert OFP_QUEUE_STATS_PACK_STR == '!IIQQQ'
        assert OFP_QUEUE_STATS_SIZE == 32
    def test_struct_ofp_group_stats_request(self):
        assert OFP_GROUP_STATS_REQUEST_PACK_STR == '!I4x'
        assert OFP_GROUP_STATS_REQUEST_SIZE == 8
    def test_struct_ofp_group_stats(self):
        assert OFP_GROUP_STATS_PACK_STR == '!H2xII4xQQ'
        assert OFP_GROUP_STATS_SIZE == 32
    def test_struct_ofp_bucket_counter(self):
        assert OFP_BUCKET_COUNTER_PACK_STR == '!QQ'
        assert OFP_BUCKET_COUNTER_SIZE == 16
    def test_struct_ofp_group_desc_stats(self):
        assert OFP_GROUP_DESC_STATS_PACK_STR == '!HBxI'
        assert OFP_GROUP_DESC_STATS_SIZE == 8
    def test_struct_ofp_group_features_stats(self):
        assert OFP_GROUP_FEATURES_STATS_PACK_STR == '!II4I4I'
        assert OFP_GROUP_FEATURES_STATS_SIZE == 40
    def test_enmu_ofp_group_capabilities(self):
        assert OFPGFC_SELECT_WEIGHT == 1 << 0
        assert OFPGFC_SELECT_LIVENESS == 1 << 1
        assert OFPGFC_CHAINING == 1 << 2
        assert OFPGFC_CHAINING_CHECKS == 1 << 3
    def test_struct_ofp_experimenter_stats_header(self):
        assert OFP_EXPERIMENTER_STATS_HEADER_PACK_STR == '!II'
        assert OFP_EXPERIMENTER_STATS_HEADER_SIZE == 8
    def test_struct_opf_queue_get_config_request(self):
        assert OFP_QUEUE_GET_CONFIG_REQUEST_PACK_STR == '!I4x'
        assert OFP_QUEUE_GET_CONFIG_REQUEST_SIZE == 16
    def test_struct_ofp_queue_get_config_reply(self):
        assert OFP_QUEUE_GET_CONFIG_REPLY_PACK_STR == '!I4x'
        assert OFP_QUEUE_GET_CONFIG_REPLY_SIZE == 16
    def test_struct_ofp_packet_out(self):
        assert OFP_PACKET_OUT_PACK_STR == '!IIH6x'
        assert OFP_PACKET_OUT_SIZE == 24
    def test_struct_ofp_role_request(self):
        assert OFP_ROLE_REQUEST_PACK_STR == '!I4xQ'
        assert OFP_ROLE_REQUEST_SIZE == 24
    def test_enum_ofp_controller_role(self):
        assert OFPCR_ROLE_NOCHANGE == 0
        assert OFPCR_ROLE_EQUAL == 1
        assert OFPCR_ROLE_MASTER == 2
        assert OFPCR_ROLE_SLAVE == 3
    def test_struct_ofp_packet_in(self):
        assert OFP_PACKET_IN_PACK_STR == '!IHBB'
        assert OFP_PACKET_IN_SIZE == 24
    def test_enum_ofp_packet_in_reason(self):
        assert OFPR_NO_MATCH == 0
        assert OFPR_ACTION == 1
        assert OFPR_INVALID_TTL == 2
    def test_struct_ofp_flow_removed(self):
        assert OFP_FLOW_REMOVED_PACK_STR == '!QHBBIIHHQQHHBBBB'
        assert OFP_FLOW_REMOVED_PACK_STR0 == '!QHBBIIHHQQ'
        assert OFP_FLOW_REMOVED_SIZE == 56
    def test_enum_ofp_flow_removed_reason(self):
        assert OFPRR_IDLE_TIMEOUT == 0
        assert OFPRR_HARD_TIMEOUT == 1
        assert OFPRR_DELETE == 2
        assert OFPRR_GROUP_DELETE == 3
    def test_struct_ofp_port_status(self):
        assert OFP_PORT_STATUS_PACK_STR == '!B7xI4x6s2x16sIIIIIIII'
        assert OFP_PORT_STATUS_DESC_OFFSET == 16
        assert OFP_PORT_STATUS_SIZE == 80
    def test_enum_ofp_port_reason(self):
        assert OFPPR_ADD == 0
        assert OFPPR_DELETE == 1
        assert OFPPR_MODIFY == 2
    def test_struct_ofp_error_msg(self):
        assert OFP_ERROR_MSG_PACK_STR == '!HH'
        assert OFP_ERROR_MSG_SIZE == 12
    def test_enum_ofp_error_type(self):
        assert OFPET_HELLO_FAILED == 0
        assert OFPET_BAD_REQUEST == 1
        assert OFPET_BAD_ACTION == 2
        assert OFPET_BAD_INSTRUCTION == 3
        assert OFPET_BAD_MATCH == 4
        assert OFPET_FLOW_MOD_FAILED == 5
        assert OFPET_GROUP_MOD_FAILED == 6
        assert OFPET_PORT_MOD_FAILED == 7
        assert OFPET_TABLE_MOD_FAILED == 8
        assert OFPET_QUEUE_OP_FAILED == 9
        assert OFPET_SWITCH_CONFIG_FAILED == 10
        assert OFPET_ROLE_REQUEST_FAILED == 11
        assert OFPET_EXPERIMENTER == 0xffff
    def test_enum_ofp_hello_failed_code(self):
        assert OFPHFC_INCOMPATIBLE == 0
        assert OFPHFC_EPERM == 1
    def test_enum_ofp_bad_request_code(self):
        assert OFPBRC_BAD_VERSION == 0
        assert OFPBRC_BAD_TYPE == 1
        assert OFPBRC_BAD_STAT == 2
        assert OFPBRC_BAD_EXPERIMENTER == 3
        assert OFPBRC_BAD_EXP_TYPE == 4
        assert OFPBRC_EPERM == 5
        assert OFPBRC_BAD_LEN == 6
        assert OFPBRC_BUFFER_EMPTY == 7
        assert OFPBRC_BUFFER_UNKNOWN == 8
        assert OFPBRC_BAD_TABLE_ID == 9
        assert OFPBRC_IS_SLAVE == 10
        assert OFPBRC_BAD_PORT == 11
        assert OFPBRC_BAD_PACKET == 12
    def test_enum_ofp_bad_action_code(self):
        assert OFPBAC_BAD_TYPE == 0
        assert OFPBAC_BAD_LEN == 1
        assert OFPBAC_BAD_EXPERIMENTER == 2
        assert OFPBAC_BAD_EXP_TYPE == 3
        assert OFPBAC_BAD_OUT_PORT == 4
        assert OFPBAC_BAD_ARGUMENT == 5
        assert OFPBAC_EPERM == 6
        assert OFPBAC_TOO_MANY == 7
        assert OFPBAC_BAD_QUEUE == 8
        assert OFPBAC_BAD_OUT_GROUP == 9
        assert OFPBAC_MATCH_INCONSISTENT == 10
        assert OFPBAC_UNSUPPORTED_ORDER == 11
        assert OFPBAC_BAD_TAG == 12
        assert OFPBAC_BAD_SET_TYPE == 13
        assert OFPBAC_BAD_SET_LEN == 14
        assert OFPBAC_BAD_SET_ARGUMENT == 15
    def test_enum_ofp_bad_instruction_code(self):
        assert OFPBIC_UNKNOWN_INST == 0
        assert OFPBIC_UNSUP_INST == 1
        assert OFPBIC_BAD_TABLE_ID == 2
        assert OFPBIC_UNSUP_METADATA == 3
        assert OFPBIC_UNSUP_METADATA_MASK == 4
        assert OFPBIC_BAD_EXPERIMENTER == 5
        assert OFPBIC_BAD_EXP_TYPE == 6
        assert OFPBIC_BAD_LEN == 7
        assert OFPBIC_EPERM == 8
    def test_enum_ofp_bad_match_code(self):
        assert OFPBMC_BAD_TYPE == 0
        assert OFPBMC_BAD_LEN == 1
        assert OFPBMC_BAD_TAG == 2
        assert OFPBMC_BAD_DL_ADDR_MASK == 3
        assert OFPBMC_BAD_NW_ADDR_MASK == 4
        assert OFPBMC_BAD_WILDCARDS == 5
        assert OFPBMC_BAD_FIELD == 6
        assert OFPBMC_BAD_VALUE == 7
        assert OFPBMC_BAD_MASK == 8
        assert OFPBMC_BAD_PREREQ == 9
        assert OFPBMC_DUP_FIELD == 10
        assert OFPBMC_EPERM == 11
    def test_enum_ofp_flow_mod_failed_code(self):
        assert OFPFMFC_UNKNOWN == 0
        assert OFPFMFC_TABLE_FULL == 1
        assert OFPFMFC_BAD_TABLE_ID == 2
        assert OFPFMFC_OVERLAP == 3
        assert OFPFMFC_EPERM == 4
        assert OFPFMFC_BAD_TIMEOUT == 5
        assert OFPFMFC_BAD_COMMAND == 6
        assert OFPFMFC_BAD_FLAGS == 7
    def test_enum_ofp_group_mod_failed_code(self):
        assert OFPGMFC_GROUP_EXISTS == 0
        assert OFPGMFC_INVALID_GROUP == 1
        assert OFPGMFC_WEIGHT_UNSUPPORTED == 2
        assert OFPGMFC_OUT_OF_GROUPS == 3
        assert OFPGMFC_OUT_OF_BUCKETS == 4
        assert OFPGMFC_CHAINING_UNSUPPORTED == 5
        assert OFPGMFC_WATCH_UNSUPPORTED == 6
        assert OFPGMFC_LOOP == 7
        assert OFPGMFC_UNKNOWN_GROUP == 8
        assert OFPGMFC_CHAINED_GROUP == 9
        assert OFPGMFC_BAD_TYPE == 10
        assert OFPGMFC_BAD_COMMAND == 11
        assert OFPGMFC_BAD_BUCKET == 12
        assert OFPGMFC_BAD_WATCH == 13
        assert OFPGMFC_EPERM == 14
    def test_enum_ofp_port_mod_failed_code(self):
        assert OFPPMFC_BAD_PORT == 0
        assert OFPPMFC_BAD_HW_ADDR == 1
        assert OFPPMFC_BAD_CONFIG == 2
        assert OFPPMFC_BAD_ADVERTISE == 3
        assert OFPPMFC_EPERM == 4
    def test_enum_ofp_table_mod_failed_code(self):
        assert OFPTMFC_BAD_TABLE == 0
        assert OFPTMFC_BAD_CONFIG == 1
        assert OFPTMFC_EPERM == 2
    def test_enum_ofp_queue_op_failed_code(self):
        assert OFPQOFC_BAD_PORT == 0
        assert OFPQOFC_BAD_QUEUE == 1
        assert OFPQOFC_EPERM == 2
    def test_enum_ofp_switch_config_failed_code(self):
        assert OFPSCFC_BAD_FLAGS == 0
        assert OFPSCFC_BAD_LEN == 1
        assert OFPSCFC_EPERM == 2
    def test_enum_ofp_role_request_failed_code(self):
        assert OFPRRFC_STALE == 0
        assert OFPRRFC_UNSUP == 1
        assert OFPRRFC_BAD_ROLE == 2
    def test_struct_ofp_error_experimenter_msg(self):
        assert OFP_ERROR_EXPERIMENTER_MSG_PACK_STR == '!HHI'
        assert OFP_ERROR_EXPERIMENTER_MSG_SIZE == 16
    def test_struct_ofp_experimenter_header(self):
        assert OFP_EXPERIMENTER_HEADER_PACK_STR == '!II'
        assert OFP_EXPERIMENTER_HEADER_SIZE == 16
    # OXM is interpreted as a 32-bit word in network byte order.
    # - oxm_class   17-bit to 32-bit (OFPXMC_*).
    # - oxm_field   10-bit to 16-bit (OFPXMT_OFB_*).
    # - oxm_hasmask  9-bit           (Set if OXM include a bitmask).
    # - oxm_length   1-bit to 8-bit  (Lenght of OXM payload).
    def _test_OXM(self, value, class_, field, hasmask, length):
        virfy = (class_ << 16) | (field << 9) | (hasmask << 8) | length
        assert value >> 32 == 0
        assert value == virfy
    def _test_OXM_basic(self, value, field, hasmask, length):
        self._test_OXM(value, OFPXMC_OPENFLOW_BASIC, field, hasmask, length)

    def test_OXM_basic(self):
        self._test_OXM_basic(OXM_OF_IN_PORT, OFPXMT_OFB_IN_PORT, 0, 4)
        self._test_OXM_basic(OXM_OF_IN_PHY_PORT, OFPXMT_OFB_IN_PHY_PORT, 0, 4)
        self._test_OXM_basic(OXM_OF_METADATA, OFPXMT_OFB_METADATA, 0, 8)
        self._test_OXM_basic(OXM_OF_METADATA_W, OFPXMT_OFB_METADATA, 1, 16)
        self._test_OXM_basic(OXM_OF_ETH_DST, OFPXMT_OFB_ETH_DST, 0, 6)
        self._test_OXM_basic(OXM_OF_ETH_DST_W, OFPXMT_OFB_ETH_DST, 1, 12)
        self._test_OXM_basic(OXM_OF_ETH_SRC, OFPXMT_OFB_ETH_SRC, 0, 6)
        self._test_OXM_basic(OXM_OF_ETH_SRC_W, OFPXMT_OFB_ETH_SRC, 1, 12)
        self._test_OXM_basic(OXM_OF_ETH_TYPE, OFPXMT_OFB_ETH_TYPE, 0, 2)
        self._test_OXM_basic(OXM_OF_VLAN_VID, OFPXMT_OFB_VLAN_VID, 0, 2)
        self._test_OXM_basic(OXM_OF_VLAN_VID_W, OFPXMT_OFB_VLAN_VID, 1, 4)
        self._test_OXM_basic(OXM_OF_VLAN_PCP, OFPXMT_OFB_VLAN_PCP, 0, 1)
        self._test_OXM_basic(OXM_OF_IP_DSCP, OFPXMT_OFB_IP_DSCP, 0, 1)
        self._test_OXM_basic(OXM_OF_IP_ECN, OFPXMT_OFB_IP_ECN, 0, 1)
        self._test_OXM_basic(OXM_OF_IP_PROTO, OFPXMT_OFB_IP_PROTO, 0, 1)
        self._test_OXM_basic(OXM_OF_IPV4_SRC, OFPXMT_OFB_IPV4_SRC, 0, 4)
        self._test_OXM_basic(OXM_OF_IPV4_SRC_W, OFPXMT_OFB_IPV4_SRC, 1, 8)
        self._test_OXM_basic(OXM_OF_IPV4_DST, OFPXMT_OFB_IPV4_DST, 0, 4)
        self._test_OXM_basic(OXM_OF_IPV4_DST_W, OFPXMT_OFB_IPV4_DST, 1, 8)
        self._test_OXM_basic(OXM_OF_TCP_SRC, OFPXMT_OFB_TCP_SRC, 0, 2)
        self._test_OXM_basic(OXM_OF_TCP_DST, OFPXMT_OFB_TCP_DST, 0, 2)
        self._test_OXM_basic(OXM_OF_UDP_SRC, OFPXMT_OFB_UDP_SRC, 0, 2)
        self._test_OXM_basic(OXM_OF_UDP_DST, OFPXMT_OFB_UDP_DST, 0, 2)
        self._test_OXM_basic(OXM_OF_SCTP_SRC, OFPXMT_OFB_SCTP_SRC, 0, 2)
        self._test_OXM_basic(OXM_OF_SCTP_DST, OFPXMT_OFB_SCTP_DST, 0, 2)
        self._test_OXM_basic(OXM_OF_ICMPV4_TYPE, OFPXMT_OFB_ICMPV4_TYPE, 0, 1)
        self._test_OXM_basic(OXM_OF_ICMPV4_CODE, OFPXMT_OFB_ICMPV4_CODE, 0, 1)
        self._test_OXM_basic(OXM_OF_ARP_OP, OFPXMT_OFB_ARP_OP, 0, 2)
        self._test_OXM_basic(OXM_OF_ARP_SPA, OFPXMT_OFB_ARP_SPA, 0, 4)
        self._test_OXM_basic(OXM_OF_ARP_SPA_W, OFPXMT_OFB_ARP_SPA, 1, 8)
        self._test_OXM_basic(OXM_OF_ARP_TPA, OFPXMT_OFB_ARP_TPA, 0, 4)
        self._test_OXM_basic(OXM_OF_ARP_TPA_W, OFPXMT_OFB_ARP_TPA, 1, 8)
        self._test_OXM_basic(OXM_OF_ARP_SHA, OFPXMT_OFB_ARP_SHA, 0, 6)
        self._test_OXM_basic(OXM_OF_ARP_SHA_W, OFPXMT_OFB_ARP_SHA, 1, 12)
        self._test_OXM_basic(OXM_OF_ARP_THA, OFPXMT_OFB_ARP_THA, 0, 6)
        self._test_OXM_basic(OXM_OF_ARP_THA_W, OFPXMT_OFB_ARP_THA, 1, 12)
        self._test_OXM_basic(OXM_OF_IPV6_SRC, OFPXMT_OFB_IPV6_SRC, 0, 16)
        self._test_OXM_basic(OXM_OF_IPV6_SRC_W, OFPXMT_OFB_IPV6_SRC, 1, 32)
        self._test_OXM_basic(OXM_OF_IPV6_DST, OFPXMT_OFB_IPV6_DST, 0, 16)
        self._test_OXM_basic(OXM_OF_IPV6_DST_W, OFPXMT_OFB_IPV6_DST, 1, 32)
        self._test_OXM_basic(OXM_OF_IPV6_FLABEL, OFPXMT_OFB_IPV6_FLABEL, 0, 4)
        self._test_OXM_basic(OXM_OF_IPV6_FLABEL_W,
                             OFPXMT_OFB_IPV6_FLABEL, 1, 8)
        self._test_OXM_basic(OXM_OF_ICMPV6_TYPE, OFPXMT_OFB_ICMPV6_TYPE, 0, 1)
        self._test_OXM_basic(OXM_OF_ICMPV6_CODE, OFPXMT_OFB_ICMPV6_CODE, 0, 1)
        self._test_OXM_basic(OXM_OF_IPV6_ND_TARGET,
                             OFPXMT_OFB_IPV6_ND_TARGET, 0, 16)
        self._test_OXM_basic(OXM_OF_IPV6_ND_SLL, OFPXMT_OFB_IPV6_ND_SLL, 0, 6)
        self._test_OXM_basic(OXM_OF_IPV6_ND_TLL, OFPXMT_OFB_IPV6_ND_TLL, 0, 6)
        self._test_OXM_basic(OXM_OF_MPLS_LABEL, OFPXMT_OFB_MPLS_LABEL, 0, 4)
        self._test_OXM_basic(OXM_OF_MPLS_TC, OFPXMT_OFB_MPLS_TC, 0, 1)

    def test_define_constants(self):
        assert OFP_VERSION == 0x03
        assert OFP_TCP_PORT == 6633
        assert MAX_XID == 0xffffffff