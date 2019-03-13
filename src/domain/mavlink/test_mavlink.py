# Internal
from src.domain.mavlink.mavlink_dialect_generator import MavlinkDialectGenerator
from src.domain.mavlink.mavlink_package_generator import MavlinkPackageGenerator
# Python

from pymavlink.generator.mavgen import mavgen, Opts


# options = Opts('/home/user/tmp/sssttt.py')

# c = mavgen(options, ['/home/user/Data/Work/Projects/pilotb/2ndparty/protocols/rulink/_dialects/altius/altius.xml'])
# c = mavgen(options, ['/home/user/tmp/sssttt.xml'])
#
# module = __import__('sssttt')
# d = module.MAVLink_attitude_message(1, 2, 3, 4, 5)
# parse = module.MAVLink(None).parse_buffer
# print(d.to_json())
# c = module.MAVLINK_MSG_ID_ATTITUDE
# data = d.pack(module.MAVLink(None))
# print(data)
#
# print(d.get_payload())
#
# f = b'\x01\x00\x00\x00\x00\x00@@\x00\x00\x80@\x00\x00\xa0@\x02'
#
# from pymavlink.generator.mavcrc import x25crc
#
# def wrapMavlinkPayload(payload):
#
#     STX = b'\xfe'
#     LEN = bytes([len(payload)])
#     SEQ = b'\x01'
#     SYS = b'\x01'
#     COMP = b'\x01'
#     MESSAGE_ID = bytes([module.MAVLINK_MSG_ID_ATTITUDE])
#     PAYLOAD = payload
#     CKA = b'\x01'
#     CKA = b'\x02'
#
#     sf = STX + LEN + SEQ + SYS+ COMP+ MESSAGE_ID+ PAYLOAD
#
#     import struct
#     crc = x25crc(sf[1:])
#     if True:  # using CRC extra
#         crc.accumulate_str(struct.pack('B', 172))
#     _crc = crc.crc
#
#
#     f = struct.pack('<H', _crc)
#
#     return sf + f
#
# # TODO: как посчитать контрольную сумму
#
# data = wrapMavlinkPayload(f)
# print(1, parse(data)[0].to_json())
#
# import sqlite3
# con = sqlite3.connect('/home/user/Data/tmp/pilotb_server')
# data = con.execute('SELECT * FROM Record WHERE PipeId = 2')

# generator = MavlinkDialectGenerator()
c = '<mavlink><version>3</version>  <dialect>0</dialect>  <enums><enum name="RELIABILITY">      <description>Data reliability.</description>      <entry name="RELIABILITY_FAILED" value="0">        <description>Data is reliabile.</description>      </entry>      <entry name="RELIABILITY_OK" value="1">        <description>Data is not reliabile.</description>      </entry>    </enum>    </enums><messages><message id="22" name="ATTITUDE">      <description>The attitude in the aeronautical frame (right-handed, Z-down, X-front, Y-right).</description>      <field name="time_boot_ms" type="uint32_t" units="ms">Timestamp (time since system boot).</field>      <field display="bitmask" enum="RELIABILITY" name="reliability" print_format="0x%04x" type="uint8_t">Reliability</field>      <field name="roll" type="float" units="rad">Roll angle in radians (-pi..+pi)</field>      <field name="pitch" type="float" units="rad">Pitch angle in radians (-pi..+pi)</field>      <field name="yaw" type="float" units="rad">Yaw angle in radians (-pi..+pi)</field>    </message>    </messages></mavlink>'
e = '<mavlink><version>3</version>  <dialect>0</dialect>  <enums><enum name="RELIABILITY">      <description>Data reliability.</description>      <entry name="RELIABILITY_FAILED" value="0">        <description>Data is reliabile.</description>      </entry>      <entry name="RELIABILITY_OK" value="1">        <description>Data is not reliabile.</description>      </entry>    </enum>    </enums><messages><message id="21" name="SNS">      <description>The satellite navigation system.</description>      <field name="time_boot_ms" type="uint32_t" units="ms">Timestamp (time since system boot)</field>      <field display="bitmask" enum="RELIABILITY" name="reliability" print_format="0x%04x" type="uint8_t">Reliability</field>      <field name="time_sns" type="uint64_t" units="ms">Satellite timestamp</field>      <field name="latitude" type="int32_t" units="degE7">Latitude (WGS84, EGM96 ellipsoid)</field>      <field name="longitude" type="int32_t" units="degE7">Longitude (WGS84, EGM96 ellipsoid)</field>      <field name="altitude" type="int32_t" units="mm">Satellite AMSL altitude</field>      <field name="groundspeed" type="float" units="m/s">Current ground speed</field>      <field name="climb" type="float" units="m/s">Satellite climb</field>      <field name="course" type="float" units="rad">Course over ground (NOT heading, but direction of movement) in radians (0..+2pi)</field>    </message>    </messages></mavlink>'
# c = generator.generate(e)

# print(c)

b = MavlinkPackageGenerator()
g = b.generatePackageFor(b'\x01\x00\x00\x00\x00\x00@@\x00\x00\x80@\x00\x00\xa0@\x02', e)
print(g.to_json())