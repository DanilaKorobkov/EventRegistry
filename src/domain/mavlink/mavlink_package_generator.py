# Internal
from src.common.decorators import private, singleton
from src.common.project_paths import pathToRuntimeGeneratedDialects
from src.domain.wrappers.mavlink_package_wrapper import MavlinkPackageWrapper
from src.domain.mavlink.mavlink_dialect_generator import MavlinkDialectGenerator
# Python
import sys
import struct
from pymavlink.generator.mavcrc import x25crc


@singleton
class MavlinkPackageGenerator:

    def __init__(self):

        self.dialect = None
        self.metaData: str = None


    def changeDialect(self, metaData):

        if self.metaData != metaData:

            self.metaData = metaData
            self.dialect = MavlinkDialectGenerator().generateUsing(metaData)


    def generatePackageFor(self, payload: bytes):

        dialectModule = self.importDialectModule(self.dialect)

        packageClass = dialectModule.mavlink_map[next(iter(dialectModule.mavlink_map))]

        fullPackage = self.wrapPayload(packageClass, payload)

        parse = dialectModule.MAVLink(None).parse_buffer
        package = parse(fullPackage)[0]

        return MavlinkPackageWrapper(package)


    @private
    def importDialectModule(self, dialect: str):

        if pathToRuntimeGeneratedDialects not in sys.path:
            sys.path.append(pathToRuntimeGeneratedDialects)

        module = __import__(dialect, globals(), locals(), ['object'], 0)
        return module


    @private
    def wrapPayload(self, packageClass, payload: bytes):

        STX = b'\xfe'
        LEN = bytes([len(payload)])
        SEQ = b'\x01'
        SYS = b'\x01'
        COMP = b'\x01'
        MESSAGE_ID = bytes([packageClass.id])
        PAYLOAD = payload

        package = STX + LEN + SEQ + SYS + COMP + MESSAGE_ID + PAYLOAD

        ckeckSum = x25crc(package[1:])
        ckeckSum.accumulate_str(struct.pack('B', packageClass.crc_extra))
        ckeckSum = ckeckSum.crc

        ckeckSum = struct.pack('<H', ckeckSum)

        return package + ckeckSum
