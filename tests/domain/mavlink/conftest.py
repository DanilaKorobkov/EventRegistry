# Internal
from tests.fakes.fake_mavlink_packages import attitudePayload, snsPayload, pilotPayload, compassPayload
# Python
import pytest



@pytest.fixture(scope = 'session')
def AttitudeMetadata():
    return """<mavlink>
   <version>3</version>
   <dialect>0</dialect>
   <enums>
      <enum name="RELIABILITY">
         <description>Data reliability.</description>
         <entry name="RELIABILITY_FAILED" value="0">
            <description>Data is reliabile.</description>
         </entry>
         <entry name="RELIABILITY_OK" value="1">
            <description>Data is not reliabile.</description>
         </entry>
      </enum>
   </enums>
   <messages>
      <message id="22" name="ATTITUDE">
         <description>The attitude in the aeronautical frame (right-handed, Z-down, X-front, Y-right).</description>
         <field name="time_boot_ms" type="uint32_t" units="ms">Timestamp (time since system boot).</field>
         <field display="bitmask" enum="RELIABILITY" name="reliability" print_format="0x%04x" type="uint8_t">Reliability</field>
         <field name="roll" type="float" units="rad">Roll angle in radians (-pi..+pi)</field>
         <field name="pitch" type="float" units="rad">Pitch angle in radians (-pi..+pi)</field>
         <field name="yaw" type="float" units="rad">Yaw angle in radians (-pi..+pi)</field>
      </message>
   </messages>
</mavlink>"""


@pytest.fixture(scope = 'session')
def SnsMetadata():
    return """<mavlink>
   <version>3</version>
   <dialect>0</dialect>
   <enums>
      <enum name="RELIABILITY">
         <description>Data reliability.</description>
         <entry name="RELIABILITY_FAILED" value="0">
            <description>Data is reliabile.</description>
         </entry>
         <entry name="RELIABILITY_OK" value="1">
            <description>Data is not reliabile.</description>
         </entry>
      </enum>
   </enums>
   <messages>
      <message id="21" name="SNS">
         <description>The satellite navigation system.</description>
         <field name="time_boot_ms" type="uint32_t" units="ms">Timestamp (time since system boot)</field>
         <field display="bitmask" enum="RELIABILITY" name="reliability" print_format="0x%04x" type="uint8_t">Reliability</field>
         <field name="time_sns" type="uint64_t" units="ms">Satellite timestamp</field>
         <field name="latitude" type="int32_t" units="degE7">Latitude (WGS84, EGM96 ellipsoid)</field>
         <field name="longitude" type="int32_t" units="degE7">Longitude (WGS84, EGM96 ellipsoid)</field>
         <field name="altitude" type="int32_t" units="mm">Satellite AMSL altitude</field>
         <field name="groundspeed" type="float" units="m/s">Current ground speed</field>
         <field name="climb" type="float" units="m/s">Satellite climb</field>
         <field name="course" type="float" units="rad">Course over ground (NOT heading, but direction of movement) in radians (0..+2pi)</field>
      </message>
   </messages>
</mavlink>"""


@pytest.fixture(scope = 'session')
def PilotMetadata():
    return """<mavlink>
   <version>3</version>
   <dialect>0</dialect>
   <enums>
      <enum name="RELIABILITY">
         <description>Data reliability.</description>
         <entry name="RELIABILITY_FAILED" value="0">
            <description>Data is reliabile.</description>
         </entry>
         <entry name="RELIABILITY_OK" value="1">
            <description>Data is not reliabile.</description>
         </entry>
      </enum>
   </enums>
   <messages>
      <message id="24" name="PILOT">
         <description>The pilot tube data.</description>
         <field name="time_boot_ms" type="uint32_t" units="ms">Timestamp (time since system boot).</field>
         <field display="bitmask" enum="RELIABILITY" name="reliability" print_format="0x%04x" type="uint8_t">Reliability</field>
         <field name="tas" type="float" units="m/s">Current true airspeed</field>
         <field name="ias" type="float" units="m/s">Current indicated airspeed</field>
         <field name="mach" type="float">Current Mach number</field>
      </message>
   </messages>
</mavlink>"""



@pytest.fixture(scope = 'session')
def CompassMetadata():
    return """<mavlink>
   <version>3</version>
   <dialect>0</dialect>
   <enums>
      <enum name="RELIABILITY">
         <description>Data reliability.</description>
         <entry name="RELIABILITY_FAILED" value="0">
            <description>Data is reliabile.</description>
         </entry>
         <entry name="RELIABILITY_OK" value="1">
            <description>Data is not reliabile.</description>
         </entry>
      </enum>
   </enums>
   <messages>
      <message id="25" name="COMPASS">
         <description>The compass data.</description>
         <field name="time_boot_ms" type="uint32_t" units="ms">Timestamp (time since system boot).</field>
         <field display="bitmask" enum="RELIABILITY" name="reliability" print_format="0x%04x" type="uint8_t">Reliability</field>
         <field name="mag_heading" type="float" units="rad">Current magnetic heading in radians (0..+2pi)</field>
         <field name="true_heading" type="float" units="rad">Current true heading in radians (0..+2pi)</field>
      </message>
   </messages>
</mavlink>"""


@pytest.fixture
def AttitudePayload(AttitudeMetadata):

    return {'metadata': AttitudeMetadata, 'data': attitudePayload}


@pytest.fixture
def SnsPayload(SnsMetadata):

    return {'metadata': SnsMetadata, 'data': snsPayload}


@pytest.fixture
def PilotPayload(PilotMetadata):

    return {'metadata': PilotMetadata, 'data': pilotPayload}


@pytest.fixture
def CompassPayload(CompassMetadata):

    return {'metadata': CompassMetadata, 'data': compassPayload}
